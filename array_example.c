#include <stdio.h>

void sum_arrays(double *result, double *a, double *b, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = a[i] + b[i];
    }
}

