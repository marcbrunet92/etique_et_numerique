#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <chrono>

using namespace std;

typedef tuple<int, int, int> Objet; // poids, valeur, index

int valeur_choix(const vector<int>& L_e, const vector<Objet>& L_objets) {
    int total = 0;
    for (int k : L_e) total += get<1>(L_objets[k]);
    return total;
}

int poids_choix(const vector<int>& L_e, const vector<Objet>& L_objets) {
    int total = 0;
    for (int k : L_e) total += get<0>(L_objets[k]);
    return total;
}

float ratio(const Objet& o) {
    return get<0>(o) != 0 ? (float)get<1>(o) / get<0>(o) : 0;
}

vector<Objet> tri(const vector<Objet>& L_objets) {
    vector<Objet> L_triee = L_objets;
    sort(L_triee.begin(), L_triee.end(), [](const Objet& a, const Objet& b) {
        return ::ratio(a) > ::ratio(b);
    });
    return L_triee;
}

tuple<vector<int>, int, int> SaD_glouton(const vector<Objet>& L_objets, int P) {
    vector<Objet> L_triee = tri(L_objets);
    vector<int> L_e;

    for (const auto& o : L_triee) {
        int idx = get<2>(o);
        if (poids_choix(L_e, L_objets) + get<0>(o) <= P) {
            L_e.push_back(idx);
        }
    }

    return { L_e, valeur_choix(L_e, L_objets), poids_choix(L_e, L_objets) };
}

tuple<vector<int>, int, int> SaD_pDyn(const vector<Objet>& L_objets, int P) {
    int n = L_objets.size();
    vector<vector<unsigned long long>> V(n, vector<unsigned long long>(P + 1, 0));

    for (int i = 0; i < n; ++i) {
        int poids = get<0>(L_objets[i]);
        int valeur = get<1>(L_objets[i]);
        for (int j = 0; j <= P; ++j) {
            if (i == 0) {
                if (j >= poids) V[i][j] = valeur;
            } else {
                if (poids > j || V[i - 1][j] > V[i - 1][j - poids] + valeur) {
                    V[i][j] = V[i - 1][j];
                } else {
                    V[i][j] = V[i - 1][j - poids] + valeur;
                }
            }
        }
    }

    // Reconstruction de la solution
    vector<int> L_e;
    int j = P;
    for (int i = n - 1; i >= 0; --i) {
        if (i > 0) {
            if (V[i][j] != V[i - 1][j]) {
                L_e.push_back(i);
                j -= get<0>(L_objets[i]);
            }
        } else {
            if (V[i][j] != 0) {
                L_e.push_back(i);
            }
        }
    }

    return { L_e, valeur_choix(L_e, L_objets), poids_choix(L_e, L_objets) };
}

int main() {
    srand((unsigned)time(0));
    int N = 100;
    vector<Objet> L_objets;
    int somme_p = 0;

    for (int i = 0; i < N; ++i) {
        float r = static_cast<float>(rand()) / RAND_MAX * 0.2f + 5.0f;
        int p = rand() % 901 + 100; // 100 à 1000
        int v = static_cast<int>(r * p);
        L_objets.emplace_back(p, v, i);
        somme_p += p;
    }

    int P = somme_p / 3;
    cout << "Poids max : " << P << endl;

    // Test glouton
    auto start1 = chrono::high_resolution_clock::now();
    auto [res_glouton, val_glouton, poids_glouton] = SaD_glouton(L_objets, P);
    auto end1 = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed1 = end1 - start1;

    cout << "Temps d'exécution (glouton): " << elapsed1.count() << " secondes" << endl;
    cout << "Valeur totale (glouton): " << val_glouton << ", Poids total: " << poids_glouton << endl;

    // Test dynamique
    auto start2 = chrono::high_resolution_clock::now();
    auto [res_dyn, val_dyn, poids_dyn] = SaD_pDyn(L_objets, P);
    auto end2 = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed2 = end2 - start2;

    cout << "Temps d'exécution (dynamique): " << elapsed2.count() << " secondes" << endl;
    cout << "Valeur totale (dynamique): " << val_dyn << ", Poids total: " << poids_dyn << endl;
    cin.get(); // Pause pour voir les résultats
    return 0;
}
