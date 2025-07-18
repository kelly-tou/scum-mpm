#include "matrix.h"

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <string.h>

#include "fixed_point.h"

// Validate that the given row and column are in bounds.
static inline bool matrix_validate(const matrix_t* matrix, const size_t row,
                                   const size_t col) {
    return row < matrix->rows && col < matrix->cols;
}

// Return the 1D array index corresponding to the given row and column.
static inline size_t matrix_index(const matrix_t* matrix, const size_t row,
                                  const size_t col) {
    return row * matrix->cols + col;
}

bool matrix_init(matrix_t* matrix, const size_t rows, const size_t cols, fixed_point_t* buffer) {
    if (rows == 0 || cols == 0) {
        return false;
    }

    matrix->rows = rows;
    matrix->cols = cols;
    matrix->buffer = buffer;

    // Zero-initialize the matrix.
    memset(matrix->buffer, 0, rows * cols * sizeof(fixed_point_t));
    return true;
}

size_t matrix_num_rows(const matrix_t* matrix) { return matrix->rows; }

size_t matrix_num_columns(const matrix_t* matrix) { return matrix->cols; }

bool matrix_get(const matrix_t* matrix, const size_t row, const size_t col,
                fixed_point_t* element) {
    if (!matrix_validate(matrix, row, col)) {
        return false;
    }

    *element = matrix->buffer[matrix_index(matrix, row, col)];
    return true;
}

bool matrix_set(matrix_t* matrix, const size_t row, const size_t col,
                const fixed_point_t value) {
    if (!matrix_validate(matrix, row, col)) {
        return false;
    }

    matrix->buffer[matrix_index(matrix, row, col)] = value;
    return true;
}

bool matrix_add(const matrix_t* matrix1, const matrix_t* matrix2,
                matrix_t* result, fixed_point_t* result_buffer) {
    const size_t num_rows = matrix1->rows;
    const size_t num_cols = matrix1->cols;

    // Validate that the input matrices have the same size.
    if (num_rows != matrix2->rows || num_cols != matrix2->cols) {
        return false;
    }

    // Initialize the result matrix.
    if (!matrix_init(result, num_rows, num_cols, result_buffer)) {
        return false;
    }

    // Add the two input matrices element-wise.
    for (size_t i = 0; i < num_rows * num_cols; ++i) {
        result->buffer[i] =
            fixed_point_add(matrix1->buffer[i], matrix2->buffer[i]);
    }
    return true;
}

bool matrix_multiply(const matrix_t* matrix1, const matrix_t* matrix2,
                     matrix_t* result, fixed_point_t* result_buffer) {
    const size_t num_rows = matrix1->rows;
    const size_t num_cols = matrix2->cols;
    const size_t inner_dimension = matrix1->cols;

    // Validate that the input matrices have compatible dimensions.
    if (inner_dimension != matrix2->rows) {
        return false;
    }

    // Initialize the result matrix.
    if (!matrix_init(result, num_rows, num_cols, result_buffer)) {
        printf("matrix multiply\n");
        return false;
    }

    // Multiple the two input matrices.
    for (size_t i = 0; i < num_rows; ++i) {
        for (size_t j = 0; j < num_cols; ++j) {
            for (size_t k = 0; k < inner_dimension; ++k) {
                result->buffer[matrix_index(result, i, j)] = fixed_point_add(
                    result->buffer[matrix_index(result, i, j)],
                    fixed_point_multiply(
                        matrix1->buffer[matrix_index(matrix1, i, k)],
                        matrix2->buffer[matrix_index(matrix2, k, j)]));
            }
        }
    }
    return true;
}

bool matrix_copy(const matrix_t* matrix, matrix_t* result, fixed_point_t* result_buffer) {
    const size_t num_rows = matrix->rows;
    const size_t num_cols = matrix->cols;
    const size_t size = num_rows * num_cols;

    // Initialize the result matrix.
    if (!matrix_init(result, num_rows, num_cols, result_buffer)) {
        return false;
    }

    memcpy(result->buffer, matrix->buffer, size * sizeof(fixed_point_t));
    return true;
}

bool matrix_transpose(const matrix_t* matrix, matrix_t* result, fixed_point_t* result_buffer) {
    const size_t num_rows = matrix->rows;
    const size_t num_cols = matrix->cols;

    // Initialize the result matrix.
    if (!matrix_init(result, num_cols, num_rows, result_buffer)) {
        return false;
    }

    fixed_point_t entry = fixed_point_init(0);
    for (size_t i = 0; i < num_rows; ++i) {
        for (size_t j = 0; j < num_cols; ++j) {
            matrix_get(matrix, i, j, &entry);
            matrix_set(result, j, i, entry);
        }
    }

    return true;
}
