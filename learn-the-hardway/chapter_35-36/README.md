#Note from the chapter

## Designing and Debugging

### Rule for `IF-STATEMENTS`
- Every `if-statement` must have an else
- if this `else` should never run because it doesn't make sense, then you must use a `die` function in the `else` that prints out an error message and dies, just like we did in chapter-35. This will find many errors
- Neve nest `if-statements` more than two deep and always try to do them one deep
- Treat `if-statements` like paragraphs, where each `if-elif-else` grouping is like a set of sentences. Put blank line before and after
- Your Boolean tests should be simple. If they are complex, move their calculation to variables earlier in your function and use a good name for the variable

### Rule for LOOPS
- Use a `while-loop` only to loop forever, and that means probably never. This only applies to Python; other languages are different.
- Use a `for-loop` for all other kinds of looping, especially if there is a fixed or limited of thins to loop over.

### Tips for DEBUGGING
- Do not use a "debugger". A debugger is like doing a full-body scan on a sick person. You do not get any specific useful information, and you find a whole lot of information that doesn't help and is just confusing
- The best way to debug a program is to use `print` to print out the values of variables at points in the program to see where they go wrong
- Make sure parts of your programs works as you work on them. Do not write massive files of code before you tray to run them. `Code a little, run a little, fix a little`

### Reading CODE
First, print out the code you want to understand. 

Second, go through your printout and take notes on the following:
- Functions and what they do.
- Where each variable is first given a value
- ANy variables with the same names in different parts of the program. These may be trouble later.
- Any `if-statements` without else clauses. Are they right?
- Any `while-loops` that might not end.
- Any parts of code that you can't understand for whatever reason.

Third, once you have all of this marked up, try to explain it to yourself by writing comments as you go. Explain the function, what variables are involved

Last, on all of the difficult parts, trace the values of each variable line by line, function by function. In fact, do another printout, and write in the margin the value of each variable that you need to “trace.”