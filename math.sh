set -f
#!/bin/bash

#Definition the variables
num1=$1
num2=$2
op=$3

#Condition to verify that variables $1 and $2 are numbers
# !:NOT
# =~: Bash operator used for regular expression
# ^[0-9]+$: regular expression
# ^: Matches the start of the string
# [0-9]: Matches digits from 0 to 9
# +: Matches one or more digits
# $: Matches the end
# ||: OR
if [[ ! $num1 =~ ^[0-9]+$ ]] || [[ ! $num2 =~ ^[0-9]+$ ]]; then
    echo "One or both inputs are not numbers"
    exit 1
fi

#Condition to make operations
if [[ $op == "+" ]]; then
    result=$((num1 + num2))
elif [[ $op == "-" ]]; then
    result=$((num1 - num2))
elif [[ $op == "/" ]]; then
    if [[ $num2 == 0 ]]; then
        echo "Error: Division by zero is not allowed"
    else
        result=$((num1 / num2))
    fi
elif [[ $op == "*" ]]; then
    result=$((num1 * num2))

else
    echo "Error"
fi

echo "The result is: $result"
