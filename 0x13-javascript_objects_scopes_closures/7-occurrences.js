#!/usr/bin/node
// function that return the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
	return list.filter((value) => (value === searchElement)).length;
};
