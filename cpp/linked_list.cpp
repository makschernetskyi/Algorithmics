#include <stdio.h>
#include <stdlib.h>




struct node{

    int data;
    struct node *next;

};

struct node* root = NULL;
int count = 0;

void insert_at_begin(int value){
    struct node *newnode = (struct node*)malloc(sizeof(struct node));

    newnode->data = value;
    count++;

    if(root==NULL){
        root = newnode;
        root->next = NULL;
        return;
    }
    newnode->next = root;
    root = newnode;

}

void insert_at_end(int value){
    struct node *newnode = (struct node*)malloc(sizeof(struct node));
    newnode->data = value;
    count++;

    if(root==NULL){
        root = newnode;
        root->next = NULL;
        return;
    }


    struct node *temp = root;

    while(temp->next!=NULL){
        temp = temp->next;
    }

    temp ->next = newnode;
    newnode->next = NULL;


}


void insert_in_middle(int value, int position){

    if(position == 0){
        insert_at_begin(value);
        return;
    }else if(position == count-1){
        insert_at_end(value);
        return;
    }

    struct node* newnode, *temp1, *temp2;

    newnode -> data = value;

    count++;

    temp1 = root;



    for(int i = 0; i < position; i++){
        temp1 = temp1->next;
    }


    newnode -> next = temp1 -> next;
    temp1 -> next = newnode;





}

void delete_from_begin(){
    struct node *temp;
    int n;


    if(root = NULL){
        printf("List is already empty");
        return;
    }

    n = root->data;
    temp = root ->next;
    free(root);
    root = temp;
    count--;




}



void delete_from_end(){
    struct node *temp1, *temp2;
    int n;

    if(root = NULL){
        printf("List is already empty");
        return;
    }

    if(root->next==NULL){
        n = root->data;
        free(root);
        root=NULL;
        return;
    }

    count--;

    temp1 = root;

    while(temp1->next != NULL){
        temp2 = temp1;
        temp1 = temp1->next;
    }


    temp2 -> next = NULL;
    n = temp1->data;
    free(temp1);



}

void delete_from_middle(int position){

    if(position == 0){
        delete_from_begin();
        return;
    }else if(position == count-1){
        delete_from_end();
        return;
    }

    struct node *temp1, *temp2;
    int n;


    count--;

    temp1 = root;

    for(int i = 0; i < position-1; i++){
        temp1 = temp1->next;
    }


    temp2 = (temp1 -> next) -> next;
    n = (temp1->next)->data;
    free(temp1->next);
    temp1 -> next = temp2;

}



struct node *find_by_value(int value){

    struct node *temp;


    while(temp->next!=NULL || temp->data!=value){
        temp = temp->next;
    }

    if(temp->data == value){
        return temp;
    }

    return NULL;


}

struct node *find_by_position(int position){


    if(position > 0 && position <count-1){
        struct node *temp;


        for(int i = 0; i< position-1; i++){
            temp = temp -> next;
        }

        return temp;
    }


    printf("index out of a range");
    return NULL;


}





int main()
{
    return 0;
}

