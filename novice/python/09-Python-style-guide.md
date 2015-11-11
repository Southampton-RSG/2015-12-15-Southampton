---
layout: page
title: Building programs with Python
subtitle: Python Style Guide
minutes: 5
---

> ## Learning Objectives {.objectives}
>
> * Python coding conventions

This is taken from [PEP-008: Python Style Guide](https://www.python.org/dev/peps/pep-0008/). 
It is a semi-official guide to Python coding conventions.

We should stick to this unless we have hard data that proves something else is better.

Basic layout is as below:

* Indent blocks using four spaces
* Keep lines less than 80 characters long
* Separate functions with two blank lines
* Separate logical chunks of long functions with a single blank line
* Put comments on lines of their own, rather than to the right of code

Here are some basic python style rules listed in a table below:

| **Rule**  | **Good** | **Bad** |
|--------------|-------------|------------|
| No whitespace immediately inside parentheses or before the parenthesis starting indexing or slicing | `max(candidates[sublist])` | `max( candidates[ sublist ] )` , `max (candidates [sublist] )` |
| No whitespace immediately before comma or colon | `if limit > 0: print minimum, limit` | `if limit > 0 : print minimum , limit` |
| Use space around arithmetic and in-place operators | `x += 3 * 5` | `x+=3*5` |
| No spaces when specifying default parameter values | `def integrate(func, start=0.0, interval=1.0)` | `def integrate(func, start = 0.0, interval = 1.0)` |
| Never use names that are distinguished only by `"l"`, `"1"`, `"0"`, or `"O"` | `tempo_long` and `tempo_init` | `tempo_l` and `tempo_1` |
| Short lower-case names for modules (i.e., files) | `geology` | `Geology` or `geology_package` |
| Upper case with underscores for constants | `TOLERANCE` or `MAX_AREA` | `Tolerance` or `MaxArea` |
| Camel case for class names | `SingleVariableIntegrator` | `single_variable_integrator` |
| Lowercase with underscores for function and method names | `divide_region` | `divRegion` |
| and member variables | `max_so_far` | `maxSoFar` |
| Use `is` and `is not` when comparing to special values | `if current is not None:` | `if current != None:` |
| Use `isinstance` when checking types | `if isinstance(current, Rock):` | `if type(current) == Rock:` |

<p align="center">
     <strong>Table 8.1: Basic Python Style Rules </strong>                                                
</p>     

             


