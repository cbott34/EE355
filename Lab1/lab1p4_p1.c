#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main (){

    FILE *infile;
    FILE *outfile;
    int pos = 0;
    int unique = 1;
    int arr[500] = {};
    int lower[500] = {};
    char ch[500] = {};

    
    // Opening files
    infile = fopen("words.txt", "r");
    outfile = fopen("out.txt", "w");
        
        // print word in file and lowercase
        while (fscanf(infile, "%s", ch) != EOF){
            for(int i = 0; i < strlen(ch); ++i){
                lower[i] = tolower(ch[i]);
            }

            for(int j = 0; j < pos; j++){
                if(strcmp(arr[j], lower)){
                    unique = 0;
                }
            }

            if(unique == 1){
                strcpy(arr[pos], lower);
                pos = pos + 1;
            }

            for(int k = 0; k < 4; k++){
                printf("%d",k);
                printf(arr[k]);
            }
    }
}