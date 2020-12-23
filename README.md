<p align="center">
  <img src="https://raw.githubusercontent.com/y0n1n1/based/master/docs/carbon.png">
</p>

--------------------------------------------------------------------
Based is a minimalist base converter, encrypter and compiler, a numpiler!

### Installation

```bash
pip3 install git@github.com:Y0N1N1/based.git
```

### Binary?

```python
import based

numpiler = based.numpiler(10, 2, encrypt="16b") # 10 -> initial base # 2 -> final base # encrypt 16b -> encrypts value as 16b code

5_in_binary = numpiler.numpile(5) # give the compiler 5

print(5_in_binary.numpiled())
# prints -> 101
```

### encrypter

the encrypter module encrypts numbers of any base through the number - exponent encryption

## formula
<p align="center">
  <img src="https://raw.githubusercontent.com/y0n1n1/based/master/docs/CodeCogsEqn.gif">
</p>
where:
<p align="center">
  <img src="https://raw.githubusercontent.com/y0n1n1/based/master/docs/CodeCogsEqn (1).gif"> is the base
</p> 
<p align="center">
  <img src="https://raw.githubusercontent.com/y0n1n1/based/master/docs/CodeCogsEqn (2).gif"> are all the digits that make up the number (already in the base)
</p> 
<p align="center">
  <img src="https://raw.githubusercontent.com/y0n1n1/based/master/docs/CodeCogsEqn (3).gif"> is the exponent (already in the base)
</p> 
<p align="center">
  <img src="https://raw.githubusercontent.com/y0n1n1/based/master/docs/CodeCogsEqn (4).gif"> is the number
</p>
## 16 bits
the 16 bits encryption codes numbers in the format:
number sign (1 bit, 0 positive 1 negative) --- number (10 bits) --- exponent sign (1 bit, 0 positive 1 negative) --- exponent (4 bits)

```python
# --- example --- #
import based

numpiler = based.numpiler(10, 2, encrypt="16b") # 10 -> initial base # 2 -> final base # encrypt 16b -> encrypts value as 16b code
5_in_binary = numpiler.numpile(5) # give the compiler 5

print(5_in_binary.encrypted())
# prints -> 0101000000010111

print(5_in_binary.pretty_encrypted())
# prints ->
  #   number sign: 0 (positive)
  #   number: 101
  #   number compiled extension: 0000000
  #   exponent sign: 1 (negative)
  #   exponent: 0111
```

since 5 is 101, and it is positive we encrypt:
0 : 101
yet we need to fill all 10 digits:
0 : 1010000000
then we need an exponent:
0 : 1010000000 : 1 : 0111
since 1010000000 (640) * 2 to the power of -7 equals 5.

## others
the encrypter module offers other encryption sizes:
| size | structure |         limits (binary)        |
|:----:|:---------:|:------------------------------:|
|   8  |  1:4:1:2  |           -120 : 120           |
|  16  |  1:10:1:4 |         -32736 : 32736         |
|  32  | 1:20:1:10 | infinity (google's calculator) |
|  64  | 1:42:1:20 | infinity (google's calculator) |
|  128 | 1:72:1:54 | infinity (google's calculator) |

### precision
