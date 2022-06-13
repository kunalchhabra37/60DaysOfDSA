---
title: 60DaysOfDSA - Day 1 Introduction
Date: 13 June, 2022
---
# My Introduction
## Why I chose Python?
Hello Everyone, I am making this repository to document my Learnings on DSA. I am doing DSA with Python as I think it is the language of Future. Python will enter into each aspect of Programming, though it be Web Devlopment, DevOps, App Devlopment and so on. Also, I have keen interest in DevOps, so I decided to do DSA in Python as it will also help me become proficient in it.

## My Introduction
Before moving on, I would like to tell that I have already did some DSA earlier and I am starting out again as I did it a long time ago and I hardly remember any. So if you are starting out, Please clear your programming basics and language basics(*I will provide at then end of this Blog*).

My main purpose of creating this repository is to Document my Learnings in Public so that others can also pick something from it and motivate to learn in Public and Contribute to the Community.

# Lists
I started with Lists in Python which is the one of the Basic Data Structure in Python. Lists are just like arrays in other languages i.e. they can store multiple values in one variable. In Python, we can there's no fixed type of array unlike other languages, so we can store any data type in list.

I believe Arrays and Strings are two most Important Topics in any Language, so I will spend next 3 days in studying about array and solving questions related to it. I will also add code samples of all the work I do in this repository Day wise.Without wasting further time, let's move ahead.

### Lists are Mutable
---
In Python Lists are mutable, i.e. we can change the value of any index in the list. 

### List Slicing
---
We can sice the list to get sub lists or sub arrays. It returns a new list. For slicing, we just use arr[start : end :step].

**The end Index is not included.**

### Copy of Lists
---
If we directly assign one list to another, it won't create a copy of the list, but both of the variables will point to same list. Hence, change in one, will automatically change the list in other variable. For the same reason, the list is by default passed as refference to a Function which means _Function can change the value of Orignal List._
To create a copy of list we can either use copy() function or list slicing. All the other mutable data types behaves simmilarly in Python.

### List Concatenation
---
We can concatenate lists in Python, just like strings in other languages using + operator. We can also concatenate list using list comprehension(_I will talk about in day 2._) and also using extend() method.

# Questions
## Reverse Array
In this question, the approach would be to iterate array backward and printing it. Another approach, that I used, is to iterate the array as it is and to insert the element at 0th index of other array.

## Min and Max of an array
To find Min and Max, we can directly use min() and max() function in Python. We can also iterate over array and keep storing the biggest and the minimum element in other variables.

## Sort Array of 0,1,2 without any algorithm
I have counted the numbers of 0,1 and 2 in the array and created another array with same number of 0,1 and 2 but in Order.

# Resurces
- [Python List Refference](https://www.w3schools.com/python/python_lists.asp)
- [Playlist I am Following](https://www.youtube.com/playlist?list=PLyqSpQzTE6M_Fu6l8irVwXkUyC9Gwqr6_)
- [Basics for Beginners](https://www.youtube.com/watch?v=wn49bJOYAZM&list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ&index=5)


_If you have reached till here, I hope we will meet at Day2 and you're gonna rock while learning in Public._
