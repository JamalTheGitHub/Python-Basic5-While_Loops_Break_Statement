# Python Basic5 While Loops & Break Statement

Prerequisite => From this tutorial onwards, it is expected that you have the following extensions in your Visual Studio Code;

1)Code Runner 2)Python

If you want to know more on how to get Python on Visual Studio Code, google it.

First thing first, create a file called called whatever you want it to be called and save it as ".py". For example like this, "PythonTutorial.py". Navigate to that file and do your coding there.

================================================================================================

<h3>While Loops</h3>

Previously, we understood the concept of <strong>for loop</strong> but now we need to understand the <strong>while loop</strong>. So what is a <strong>while loop</strong>? Let us look at the previous example for <strong>for loop</strong> and compare them to <strong>while loop</strong>;

<strong>for loop</strong>

    total = 0
    for i in range(1,5):
      total += i

    print(total)

=====================

<strong>while loop</strong>

    total = 0
    i = 1
    while i < 5:
      total += i
      i += 1
    
    print(total)


Now if we run both codes, we would get the same output which is 10. Looking at the <strong>while loop</strong>, the difference between <strong>while loop</strong> and <strong>for loop</strong> is the functionality of it. We will talk about it later but for now, let us focus on the mechanics of <strong>while loop</strong>. Given the above example for <strong>while loop</strong>, we start by assigning <strong>total = 0</strong> because the variable <strong>total</strong> will hold the sum of few numbers which we will define later. Afterwards, assign a new variable, <strong>i = 1</strong> because we will be calling variable<strong>i</strong> again for the <strong>while loop</strong> function. If variable<strong>i</strong> is not defined, therefore the <strong>while loop</strong> function will not work. All will be clear soon as you follow along the tutorial. Alright, now is the time where we will call <strong>i</strong> in the <strong>while loop</strong> with the following code, <strong>while i < 5:</strong>. This simply means <strong>while i is less than 5</strong> do something inside the function and thus we implement the conditions of what would happen if <strong>i is less than 5</strong>. Therefore, inside the function, we define <strong>total = total + i</strong> or <strong>total += i</strong> which is the same thing. After that we include <strong>i += 1</strong> to increase the value of <strong>i</strong> until it has been <strong>5</strong> or more in order to stop the loop. In layman's term, according to the <strong>while loop</strong> function that we created, add the value of <strong>i</strong> to the <strong>total</strong> as long as <strong>i is less than 5</strong>. That is basically it. In order to be sure that we will get the desired output, print the output of total as <strong>print(total)</strong>. You should get 10 because <strong>1 + 2 + 3 + 4</strong>.

The question now is, when should we use the <strong>while loop</strong>? It should be use when you do not know how many loops you need beforehand. Here is an example;

    a = [5,4,4,3,1,-1,-1,-3,-4,-5]
    total = 0
    i = 0

    while a[i] > 0:
      total += a[i]
      i += 1

    print(total)

Now let's figure out what is going on there. First we attached a <strong>list</strong> to variable <strong>a</strong>. Then as usual, with <strong>total = 0</strong>. However we also defined variable <strong>i</strong> to be 0. Looking at the <strong>while function</strong>, notice <strong>while a[i] > 0:</strong>. Do you remember what <strong>a[i]</strong> stands for? If you forgot, kindly refer to the <strong>list</strong> topic that we covered before. Basically, it just means to select the <strong>element</strong> in the <strong>list</strong>. <strong>a[i]</strong> OR <strong>a[0]</strong> refers to the first <strong>element</strong> in the <strong>list</strong> which is 5. Notice also that the <strong>element</strong> has to be bigger than 0. Thus we can proceed to the next line where <strong>total += a[i]</strong> to store the sum of numbers that are greater than 0. <strong>i += 1</strong> just proceeds to the next <strong>element</strong> until it reaches the <strong>element</strong> that is < 0. In the case of the above example, if we run the code, we will get the output of <strong>17</strong> because  <strong>5 + 4 + 4 + 3 + 1</strong>.

Alright, what if we use the same example but without the negative numbers like this;

    a = [5,4,4,3,1]
    total = 0
    i = 0

    while a[i] > 0:
      total += a[i]
      i += 1

    print(total)

Now run the code and see what happens. We will actually get an error, <strong>IndexError</strong> to be exact. This is because we already defined the <strong>while loop</strong> to keep going with the line <strong>i += i</strong> which when it reaches the last <strong>element</strong> that is 1, it will try to go to the next <strong>element</strong> which does not exist because we did not include it in the <strong>list</strong> thus giving us the description, <strong>list index out of range</strong> attached to <strong>IndexError</strong>. In order to fix this we need to modify our example to look like;

    a = [5,4,4,3,1]
    total = 0
    i = 0

    while i < len(a) and a[i] > 0:
      total += a[i]
      i += 1
    print(total)

Notice we modify the <strong>while loop</strong> to be <strong>while i < len(a) and a[i] > 0:</strong>. <strong>len()</strong> is a pre-defined function in <strong>python</strong> which in this example we use to compute the number of indexes a <strong>list</strong> might have. <strong>len</strong> stands for length in case you are wondering and <strong>indexes</strong> are just the numbers that are assigned to the <strong>elements</strong> within the <strong>list</strong> starting for 0. For example, <strong> index 0</strong> refers to the <strong>element 5</strong> in the example above. <strong>and</strong> is used to join conditions specified whilst making the function.

How about if we use the <strong>for loop</strong> function to replicate the the same purpose? Like;

      a = [5,4,4,3,1,-1,-1,-3,-4,-5]
      total = 0

Can we total up only the positive numbers using <strong>for loop</strong>? Yes definitely! With that it will look something like this;

      a = [5,4,4,3,1,-1,-1,-3,-4,-5]
      total = 0

    for num in a:
      if num <= 0:
        break
      total += num
    print(total)

Notice in the <strong>if</strong> statement we specified that if <strong>num</strong> is lesser or equals to zero, <strong>break</strong>. <strong>break</strong> means to stop the loop from moving on thus only the positive numbers will be taken into account. However can we also use the <strong>break</strong> in <strong>while loop</strong>? The answer is yes! We will take the same example as above but for <strong>while loop</strong>.

    a = [5,4,4,3,1,-1,-1,-3,-4,-5]
    total = 0
    i = 0

    while True:
      total += a[i]
      i += 1
      if a[i] <= 0:
        break

    print(total)

We use <strong>while True</strong> because we need a <strong>true</strong> statement for the purpose of this example. Notice that <strong>True</strong> is with the capital "T" because it is pre-defined that way in <strong>Python</strong>. Anyways, looking at the code, we understand the flow that <strong>elements</strong> will keep adding together until it reaches the <strong>if statement</strong> where it says if the <strong>element</strong> is less or equals to 0, break the loop. Thus by running the code, we will get the output of 17.

================================================================================================

Okay now is to test your understanding so far into Python! Here is an exercise for you;

    a = [6,5,4,3,1,-1,-4,-5,-7,-7]

Your task is to total up the negative numbers with <strong>while loop</strong> and <strong>for loop</strong>.