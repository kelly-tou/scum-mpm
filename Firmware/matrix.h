// The matrix represents a statically sized 2D matrix using a 1D array.

#ifndef __MATRIX_H
#define __MATRIX_H

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

#include "fixed_point.h"

// // Maximum number of elements (i.e., rows x columns) in the matrix.
// #define MATRIX_MAX_SIZE 512

// Matrix element type.
typedef fixed_point_t matrix_type_t;

// Matrix struct.
typedef struct {
    // Number of rows.
    size_t rows;

    // Number of columns.
    size_t cols;

    // Matrix buffer.
    // fixed_point_t buffer[MATRIX_MAX_SIZE];
    fixed_point_t* buffer;
} matrix_t;

// Initialize a matrix with the given number of rows and columns. By default,
// the matrix will be zero-initialized. Return whether the matrix was
// successfully initialized.
bool matrix_init(matrix_t* matrix, size_t rows, size_t cols, fixed_point_t* buffer);

// Get the number of rows in the matrix.
size_t matrix_num_rows(const matrix_t* matrix);

// Get the number of columns in the matrix.
size_t matrix_num_columns(const matrix_t* matrix);

// Get the matrix element at the specified row and column.
// Return whether the matrix element was successfully accessed.
bool matrix_get(const matrix_t* matrix, size_t row, size_t col,
                fixed_point_t* element);

// Set the matrix element at the specified row and column to the given value.
// Return whether the matrix element was successfully set.
bool matrix_set(matrix_t* matrix, size_t row, size_t col, fixed_point_t value);

// Add two matrices together, writing the result to another matrix.
// The result matrix does not need to be initialized.
// Return whether the matrix addition was successful.
bool matrix_add(const matrix_t* matrix1, const matrix_t* matrix2,
                matrix_t* result, fixed_point_t* result_buffer);

// Multiply two matrices together, writing the result to another matrix.
// The result matrix does not need to be initialized.
// Return whether the matrix multiplication was successful.
bool matrix_multiply(const matrix_t* matrix1, const matrix_t* matrix2,
                     matrix_t* result, fixed_point_t* result_buffer);

// Copy a matrix, writing the result to another matrix.
// The result matrix does not need to be initialized.
// Return whether the matrix copying was successful.
bool matrix_copy(const matrix_t* matrix, matrix_t* result, fixed_point_t* result_buffer);

// Tranpose a matrix, writing the result to another matrix.
// The result matrix does not need to be initialized.
// Return whether the matrix transpose was successful.
bool matrix_transpose(const matrix_t* matrix, matrix_t* result, fixed_point_t* result_buffer);

#endif  // __MATRIX_H
