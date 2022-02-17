<h1>NumPy Cheat Sheet</h1>

This document outlines a list of useful [NumPy](https://numpy.org/) operations and functions.

<h2>Contents</h2>

[toc]

## Installation

### Virtual Environment (optional)

```bash
# Create virtual environment
python3 -m venv env
# Activate virtual environment (Linux/MacOS)
source env/bin/activate
# Activate virtual environment (Windows)
source env/Scripts/activate
```

### Numpy Installation

```bash
pip3 install numpy
```

### Importing NumPy

Import NumPy in a Python script or shell session:

```python
import numpy as np
```

## Array Creation

### Array From List

Create array from list `[3, 1, 4, 5, 9]`:

```python
>>> np.array([3, 1, 4, 1, 5, 9], dtype=np.float64)
array([3., 1., 4., 1., 5., 9.])
```

### Array with Values

#### Zeros

Create array of shape `(2, 3)` and fill with zeros:

```python
>>> np.zeros((2, 3), dtype=np.float64)
array([[0., 0., 0.],
       [0., 0., 0.]])
```

#### Ones

Create array of shape `(2, 3)` and fill with ones:

```python
>>> np.ones((2, 3), dtype=np.float64)
array([[1., 1., 1.],
       [1., 1., 1.]])
```

#### Arbitrary

Create array of shape `(2, 3)` and fill with `42`:

```python
>>> np.full((2, 3), 42, dtype=np.float64)
array([[42., 42., 42.],
       [42., 42., 42.]])
```

#### Uninitialized

Create array of shape `(2, 3)` with uninitialized values:

```python
>>> np.empty((2, 3), dtype=np.float64)
array([[2.00000000e+000, 2.00000000e+000, 2.17694310e-314],
       [2.17695485e-314, 2.18452430e-314, 4.17201348e-309]])
```

### Other Special Arrays

#### Random

Create array of shape `(2, 3)` with random values ranging between `0` and `1`:

```python
>>> rng = np.random.default_rng()
>>> rng.random((2, 3), dtype=np.float64)
array([[0.91311565, 0.44918684, 0.7825793 ],
       [0.54252955, 0.38151146, 0.68711842]])
```

#### Evenly Spaced

Create array of evenly spaced values from `0` to `5`:

```python
>>> np.arange(5, dtype=np.float64)
array([0., 1., 2., 3., 4.])
```

Create array of evenly spaced values from `0` to `10` with step size `2`:

```python
>>> np.arange(0, 10, 2, dtype=np.float64)
array([0., 2., 4., 6., 8.])
```

Create array of `6` evenly spaced values from `0` to `5` (including `5`):

```python
>>> np.linspace(0, 5, 6, dtype=np.float64)
array([0., 1., 2., 3., 4., 5.])
```

#### Identity Matrix

Create `3x3` identity matrix array:

```python
>>> np.eye(3, dtype=np.float64)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```

Create `2x3` identity matrix array:

```python
>>> np.eye(2, 3, dtype=np.float64)
array([[1., 0., 0.],
       [0., 1., 0.]])
```

## Data Types

### Boolean

Data type | Description
--- | ---
`np.bool_` | Boolean

### Integer

Data type | Description
--- | ---
`np.int8` | 8-bit integer
`np.int16` | 16-bit integer
`np.int32` | 32-bit integer
`np.int64` | 64-bit integer
`np.uint8` | 16-bit unsigned integer
`np.uint16` | 16-bit unsigned integer
`np.uint32` | 16-bit unsigned integer
`np.uint64` | 16-bit unsigned integer

### Floating Point Number

Data type | Description
--- | ---
`np.float16` | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
`np.float32` | Single precision float: typically sign bit, 8 bits exponent, 23 bits mantissa
`np.float64` | Double precision float: typically sign bit, 11 bits exponent, 52 bits mantissa

### Other Types

Data type | Description
--- | ---
`np.complex64` | Complex number, represented by two single-precision floats
`np.complex128` | Complex number, represented by two double-precision floats
`np.bytes_` | Byte string
`np.str` | Unicode string
`np.datetime64` | Datetime object
`np.timedelta64` | 64-bit integer timedelta
`np.object_` | Any Python object

## Array Properties

```python
>>> a = np.zeros((2, 3))
>>> a
array([[0., 0., 0.],
       [0., 0., 0.]])
```

### Dimensions

Get array dimensions:

```python
>>> a.shape
(2, 3)
>>> np.shape(a)
(2, 3)
```

Get number of array dimensions:

```python
>>> a.ndim
2
>>> len(a.shape)
2
```

Get number of elements in array across all dimensions:

```python
>>> a.size
6
```

### Data Type

Get array data type:

```python
>>> a.dtype
dtype('float64')
```

## Array Indexing & Slicing

```python
>>> a = np.arange(8)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7])
>>> b = np.arange(16).reshape((4, 4))
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15]])
```

### Indexing

Get array element at index `1`:

```python
>>> a[1]
1
```

Get array element at row index `1` and column index `2`:

```python
>>> b[1, 2]
6
>>> b[1][2]
6
```

### Slicing

Get array elements between indices `1` and `4` (exclusive):

```python
>>> a[1:4]
array([1, 2, 3])
```

Get array elements between indices `1` and `-2` (second last element exclusive):

```python
>>> a[1:-2]
array([1, 2, 3, 4, 5])
```

Get array elements after (and including) index `2`:

```python
>>> a[2:]
array([2, 3, 4, 5, 6, 7])
```

Get array elements before (and excluding) index `5`:

```python
>>> a[:5]
array([0, 1, 2, 3, 4])
```

Get array elements between row indices `1` and `3` (exclusive) and column indices `0` and `3` (exclusive):

```python
>>> b[1:3, :3]
array([[ 4,  5,  6],
       [ 8,  9, 10]])
```

Get array elements between all rows indices and column indices `1` and `4` (exclusive):

```python
>>> b[:, 1:4]
array([[ 1,  2,  3],
       [ 5,  6,  7],
       [ 9, 10, 11],
       [13, 14, 15]])
```

### Integer & Boolean Mask Indexing

Get array elements at index `0` and `-1` (last element):

```python
>>> a[[0, -1]]
array([0, 7])
```

Get even array elements (note that this flattens a multi-dimensional array):

```python
>>> b[b % 2 == 0]
array([ 0,  2,  4,  6,  8, 10, 12, 14])
```

## Array Operations

### Mathematical Operations