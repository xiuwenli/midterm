# midterm
# Fall 2018 TRGN510 Midterm
## Please provide your name below
`FirstName LastName`
** Due 10/28/18 by 11:59PM Pacific Time Zone **
  
This is an Markdown document and your exam. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. Please EMAIL ME the Readme.md file to turn it on - davidwcr@usc.edu.  This will be your completed exam.

There are different types of questions.  The first are multiple choice, fill in blank or true false.  The second are code block.Please edit the markdown such by either (1) striking *italicized* words that are incorrect using ~~strikethrough~~ (\~\~strikethrough\~\~), (2) deleting the incorrect *italicized* terms, or (3) putting the correct answer where requested.

See below for an example.  We see that both _true_ and _false_ are options.  To answer the question, we delete _false_

## Example 1

**Before the exam**
  
  * It is __true__ __false__ that the earth is round and the average temperature of the earth has risen within our lifetime

**After you edited by deleting __false__ or crossing it out, any one of these is ok**
  * It is __true__ that the earth is round and the average temperature of the earth has risen within our lifetime
* It is __true__ ~~_false_~~ that the earth is round and the average temperature of the earth has risen within our lifetime
## Example 2 - Codeblock edit
How would I list the files in my home directory, ordered by size such that the lowest size are at the bottom, and print the size of the files in a human readable format listing on the last 10 lines?
  * In this you would start with an empty codeblock, and then you would edit it so that correct commands work within R.
Before:
  ```
echo "I haven't answered and so this comment is here"
```
After
```{bash, echo = FALSE}
ls -lSh ~ | tail
```
## Types of data (any language): 14 points
* "2" is a __String__ datatype.
* 2 is a __Integer__ datatype.
* 2.05 is an __Float__ datatype.
* 3.0 is an __Float__ datatype.
* "" is an __Null__ datatype.
* "false" is an __String__ datatype.
* TRUE is an __Boolean__ datatype.

## Types of data (R)
* When we run the command *a<-c("d",1,"b")* in *R*, creates a __array__ stored in *a*.
* After we create a variable *a* and fill it with data using the command a<-c("d",1,"b"), we can subset to *d<-a[2]*.  The type of data found in *d* is of type __integer__.
* Put within the code block a command for loading in the ggplot2 library.  You may have to install.packages first - I do not expect that in the code block.  Then put in a command that creates a dataframe called "diamonds_dataframe" using the diamond function.  Then put in a command that prints out the mean of the price.  The code block should have around 3 lines - but as long as the mean of the price is provided, it is correct even with fewer lines
```{r}
library(ggplot2)
# Create a vector.
diamonds_dataframe<-diamonds

# Find mean
result.mean <- mean(diamonds_dataframe$price)
print(result.mean)

# answer:3932.8
```
If you were to load in the diamonds dataset from the ggplot2 library, what type of data is found within diamonds$carat?
  >  __numeric__
* Please make a violin plot from the diamond dataset where the X-axis is "cut" and Y-axis is "price"
```{r, echo = FALSE}
library(ggplot2)
# Basic violin plot
p <- ggplot(diamonds, aes(x=cut, y=price)) + 
  geom_violin()
print(p)

```
*These questions may involve concepts that you don't know exactly because the point is to be
able to solve new questions.  Thus to an extent you are expected to may need a little research.*
* csv files are typically __comma__ deliminited
* The data below is typically __tsv__?
> data ={
name: "John",
address: {
street: "459 E Jon St.",
city: "Springfield,
state: "Illinois",
},
age:14
}
* In the example above, data.age is __Integer__ data-type

## BASH 
You are expected to complete these by logging into the bioinform.io server. However, where indicated please place the answer in the markdown document.  In some cases, some points will be given for actions done on the server.
### What is your current path?
```{bash, echo = FALSE}
echo "pwd"
# /home/xiuwenli
```
### What is the date?
```{bash, echo = FALSE}
echo "date"
# Fri Oct 26 01:18:45 UTC 2018
```
### Please make a new directory under your home directory called midterm 
Please complete on server and fill answer below (e.g. path `~/midterm`)
```{bash, echo = FALSE}
echo "mkdir midterm"
```
### Please add the ~/midterm to your PATH variable within your `~/.bashrc` settings using vim.
Please edit the PATH variable in your `~/.bashrc` settings using vim, such that you do not need to type the full path when running commands.
```{bash, echo = FALSE}
vim ~/.bashrc
# add the code at the bottom 
# export PATH=$PATH:/home/xiuwenli/midterm
# esc 
# :wq
```

### Simple Script
Please create a simple bash script within ~/midterm called `makeupper` that takes the user input from STDIN and converts the text to all capital letters.
Thus `echo "shoutatme" | makeupper` would print `SHOUTATME`
```{bash, echo = FALSE}
#!/bin/bash

echo What you want to type?

read type
VAR1=$type
VAR2=${VAR1^^}

echo $VAR2"

```
###  What are the last 5 commands you have in your history
```{bash, echo = FALSE}
echo "history | tail -5"
# 998  cd ..
# 999  vim .bashrc
# 1000  exit
# 1001  history
# 1002  history | tail -5
```
### Please put the following data into a file called "~/midterm/numbers.txt" using bash where each number is on its own line using echo and the appropriate optional tag.
```
1234
12121
3434
123
12341239879
```
```{bash, echo = FALSE}
#!/bin/bash
echo "1234 12121 3434 123 12341239879" | xargs -n1
```

### How many characters and how many lines are in the file?
```{bash, echo = FALSE}
wc -m numbers.txt
wc -l numbers.txt
# answer 280 4
```
### Solving new concepts
Please create bash or bash set of lines using anything from sed, nawk, python or etc to commify the list of numbers in thousands place to the screen. You will need to use commands you haven't used before,  For example: 1,234 or 12,121
```{bash, echo = FALSE}
#!/bin/bash
printf "1234\n12121\n3434\n123\n12341239879\n" \ | awk '{ len=length($0); res=""; for (i=0;i<=len;i++) { res=substr($0,len-i+1,1) res; if (i > 0 && i < len && i % 3 == 0) { res = "," res } }; print res }'| xargs -n1
```
### Please make the 'numbers.txt' file private such that only you can read and write it.  Nobody at the group level can read it, write or execute it.
```{bash, echo = FALSE}
cd midterm
touch numbers1.txt
chmod 700 numbers1.txt
ls -l
```

### Please make the file 'numbers.txt' such that you can read and write to it, and everyone else on the computer both world and group can just read it.
```{bash, echo = FALSE}
cd midterm 
touch numbers2.txt
chmod 744 numbers2.txt"
ls -l
```

### Question:  How would I find all the files ending in `.sh` within my home directory or any sub-directory?
```{bash, echo = FALSE}
cd ~
find /home/xiuwenli/ -name "*.sh"
find /home/xiuwenli/subdirectory/ -name "*.sh"
```
### Question:  Please put all in the previous commands in your history into a file and call that file "~/midterm/history.txt"
```{bash, echo = FALSE}
cd ~
cd midterm
history > history.txt"
```
### Question:  Please print the first 5 lines of your history by piping history into head
```{bash, echo = FALSE}
head -n 5 history.txt # see the first 5 lines of history in history.txt
history | head -5 # see the first 5 lines of my history
```

## R
For the following you will need access to the cars dataset within R, and these will be done within R Studio.  Please make sure to load the ggplot2 library

###  Please generate a scatterplot of mpg vs hp, coloring by class
```{R, echo = FALSE}
library(ggplot2)
mtcars$names=rownames(mtcars)
ggplot(mtcars, aes(x = mpg, y = hp)) +
    geom_point(aes(color = factor(mtcars$names)))
```

###  Please make a histogram of hwy
```{R, echo = FALSE}
library(ggplot2)
hist(mpg$hwy)
```

### Please make a bar chart of class, colored by drv
```{R, echo = FALSE}
library(ggplot2)
g <- ggplot(mpg, aes(class))
g + geom_bar(aes(fill = drv))
```

## R/Shiny
For this part, you are expected to provide a URL to the following question.  
Please make a Shiny application that allows us to generate a violin plot of each different cateogrical data-type
for each continious datatype (e.g. hwy), coloring only by datatypes that are categorical in nature.
Please add a button that allows one to facet by one other categorical datatype such as class.
```{R, echo = FALSE}
library(shiny)
library(ggplot2)
#example data
dataset <- mpg
headerNames=colnames(dataset)
# Define UI for application that draws a histogram
ui <- fluidPage(
  pageWithSidebar(
    
   # Application title
   headerPanel("Data Explorer"),
    
   # Sidebar with a slider input for number of bins 
   sidebarPanel(
     selectInput('x', 'X', c("Displ" = "displ", "Years" = "year", "Cyl" = "cyl", "Cty" = "cty", "Hwy" = "hwy")),
     selectInput('y', 'Y', c("Displ" = "displ", "Years" = "year", "Cyl" = "cyl", "Cty" = "cty", "Hwy" = "hwy")),
     selectInput('color', 'Color', c("Manufacturer" = "manufacturer", "Model" = "model", "Trans" = "trans", "Drv" = "drv", "Fl" = "fl", "Class" = "class")),
     checkboxInput('geom_violin', 'geom_violin')
   ),
     # Show a plot of the generated distribution
     mainPanel(
       plotOutput("plot")
     )
   )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
   
   output$plot <- renderPlot({
     p <- ggplot(dataset, aes_string(x=input$x, y=input$y, fill=input$color))
     if (input$geom_violin)
       p <- p + geom_violin(aes_string(x=input$x, y=input$y))
     print(p)

   })
}

# Run the application 
shinyApp(ui = ui, server = server)
```
## Python
Please create a python script that will take two arguments: a regex string and a filename. The python script will printout matches within the file going line by line. Please place this in your midterm directory
`LearnRegularExpressions.py "^([0-9A-Z])\s+" Homo_sapiens.GRCh37.75.gtf`
will produce
`['1']`
`['1']`
`['1']`
`... and so forth`
```{bash, echo = FALSE}
#!/usr/bin/python
import fileinput
import re

for line in fileinput.input (['/home/xiuwenli/midterm/Homo_sapiens.GRCh37.75.gtf']):
    geneline = re.findall(r'^([0-9A-Z])\s+', line)
    if geneline:
       print geneline
```
