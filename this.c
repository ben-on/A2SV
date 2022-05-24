#include <stdio.h>
#include <stdlib.h>

 /*enumeration for all the states of dfa*/
enum States
{
    NORMAL, SLASH, STARBG, STARED, DQUOTE, SQUOTE, BSLASH, DQ_BSLASH, SQ_BSLASH, S_BSLASH 
};

 /* the following are functions to handle each of dfa states*/

/*normal state*/
void handler_of_normal_state(int character,enum States *state){
    if(character  =='/'){
        *state = SLASH;
    }
    else if(character  == '"'){
        *state = DQUOTE;
        putchar(character);
    }
    else if(character  == '\''){
        *state = SQUOTE;
        putchar(character);
    }
    else if(character  == '\\'){
        *state = BSLASH;
    }
    else{
        *state = NORMAL;
        putchar(character);
    }
}
/*slash state*/
void handler_of_slash_state(int character,enum States *state){
    if(character == '*'){
        *state = STARBG;
        putchar(' ');
    }
    else if(character == '/'){
        *state = SLASH;
        putchar(character);
    }
    else{
        *state = NORMAL;
        putchar('/');
        putchar(character);
    }
}
/*starbg state*/
void handler_of_starbg_state(int character,enum States *state){
    if(character == '*'){
        *state = STARED;
    }
    else if(character == '\\'){
        *state = S_BSLASH;
    }
    else{
        *state = STARBG;
    }
}
/*stared state*/
void handler_of_stared_state(int character,enum States *state){
    if(character == '/'){
        *state = NORMAL;
    }
    else if(character == '*'){
        *state = STARED;
    }
    else{
        *state = STARBG;
    }

}
/*dquote state*/
void handler_of_dquote_state(int character,enum States *state){
    if(character == '"'){
        *state = NORMAL;
        putchar(character);
    }
    else if(character == '\\'){
        *state = DQ_BSLASH;
    }
    else{
        *state = DQUOTE;
        putchar(character);
        
    }

}
/*squote state*/
void handler_of_squote_state(int character,enum States *state){
    if(character == '\''){
        *state = NORMAL;
        putchar(character);
    }
    else if(character == '\\'){
        *state = SQ_BSLASH;
    }
    else{
        *state = SQUOTE;
        putchar(character);
    }

}
/* bslash state*/
void bhandler_of_slash_state(int character,enum States *state,int *line){
    if(character =='n'){
        *state = NORMAL;
        putchar('\n');
        (*line)++;
    }
    else{
        *state = NORMAL;
        putchar('\\');
        putchar(character);
    }
}
/* dq_bslash state*/
void dq_bhandler_of_slash_state(int character,enum States *state,int *line){
    if(character =='n'){
        putchar('\n');
        (*line)++;
    }
    else{
        putchar('\\');
        putchar(character);
    }
    *state = DQUOTE;
}
/*sq_bslash state*/
void sq_bhandler_of_slash_state(int character,enum States *state,int *line){
    if(character =='n'){
        putchar('\n');
        (*line)++;
    }
    else{
        putchar('\\');
        putchar(character);
    }
    *state = SQUOTE;
}
/*s_bslash state*/
void s_bhandler_of_slash_state(int character,enum States *state,int *line){
    if(character =='n'){
        putchar('\n');
        (*line)++;
    }
    else{
        putchar('\\');
        putchar(character);
    }
    *state = STARBG;
}


 /*here is the function that identify the state of dfa and perform an action */
int checkState(int character ,enum States *state, int *line){
    if(character =='\n'){ 
            (*line)++;
    }
    if(*state == NORMAL){
        
        handler_of_normal_state(character,state);
    }
    else if(*state == SLASH){
         
         handler_of_slash_state(character,state);
    }
    else if(*state == STARBG){
         
         handler_of_starbg_state(character,state);
    }
    else if(*state == STARED){
         
         handler_of_stared_state(character,state);
    }
    else if(*state == DQUOTE){
         
         handler_of_dquote_state(character,state);
    }
    else if(*state == SQUOTE){
         
          handler_of_squote_state(character,state);
    }
    else if(*state == BSLASH){
         
         bhandler_of_slash_state(character,state,line);
    }
    else if(*state == DQ_BSLASH){
         
         dq_bhandler_of_slash_state(character,state,line);
    }
    else if(*state == SQ_BSLASH){
         
         sq_bhandler_of_slash_state(character,state,line);
    }
    else if(*state == S_BSLASH){
         
         s_bhandler_of_slash_state(character,state,line);
    }
}

 /* here is the main function decomment the provided input based on the whether the input is from stdin or file
 first it initialize enum, line number, and character variable then it will decomment the input*/
int main(int argc, char *argv[]){
    FILE  *file;
    
    enum States state;
    state=NORMAL;
    
    int line = 0;
    
    int character;
    
    /*decommenting when the input is from stdin*/
    if(argc==1) {
        /*Decomment the input*/
		while ((character=getchar())!=EOF){
            checkState(character,&state, &line);
        }
	} 
    
    /*decommenting when the input is from a file*/
    else if(argc==2) {
        
		file = fopen(argv[1], "r");
        
		if(file == NULL) {
            fprintf(stderr, "Cannot open the file\n");
            exit(-1);
		}
        
        while ((character=getc(file))!=EOF){
            checkState(character,&state, &line);
        }
        
        fclose(file);
    }   
  
  /*here is the code to handle unterminated comment and Print error line to stderr*/
        if(state == STARBG || state == STARED){
            
            fprintf(stderr, "Error: line %d: unterminated comment\n",line);
            exit(-1);     
  }
  return 0;
}