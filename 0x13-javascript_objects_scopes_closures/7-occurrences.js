#!/usr/bin/node
// function that return the number of occurrences in a list

exports.nbOccurences = function (list, searchElement){
    let i;
    let j = 0;
    for (let i = 0; i < list.length; i++) {
        if (list[i] === searchElement) {
           j = j + 1;
        }
    }
    return (j);
}
