
##Problem 1 : Splicing second occurence of a String 
''' Deccription : S="12abc6789abcdefgh" needs to be 12abc6789###defgh but with str.replace(str[9:11], "###") It Produces 
12###6789###defgh'''

##Solution 
S="12abc6789abcdefgh"
S=("").join(S[:9],"###",S[12:]


