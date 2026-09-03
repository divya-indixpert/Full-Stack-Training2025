#include <stdio.h>
#include <string.h>


char reg_username[20];
char reg_password[20];
char email_id[20];
char username[20];
char password[20];
char mobile_no[12];
char Source_city[25];
char Destination_city[25];
char number[10]={0};
int Total_seats =50;
int Payment =1500;
int Bus_number;
int Seats;
int Choice;
int Ticket_no;
int i;
int invalid;

void onlynumber();
void signup();
int login();
void bookticket();
void cancelticket();
void checkstatus();


int main()
{
  

    printf("===== BUS RESERVATION SYSTEM =====\n");
    printf("\n1 signup");
    printf("\n2. Login");
    printf("\n3. Exit");
    printf("\nPlease enter your choice:");
    scanf("%d", &Choice);
   if (Choice== 1)
   {
    signup();   

    if (login() == 0)
    {
        printf("\nLogin Failed! Program Exit.");
        return 0;
    }
   }
   
 do
    {
        printf("\n\n1. Book a Ticket");
        printf("\n2. Cancel Ticket");
        printf("\n3. Check Status");
        printf("\n4. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &Choice);

        switch (Choice)
        {
        case 1:
            bookticket();
            break;

        case 2:
            cancelticket();
            break;

        case 3:
            checkstatus();
            break;

        case 4:
            printf("\nThank you!");
            break;

        }

    } while (Choice != 4);

    return 0;
}

void signup()
{

    while (1)
    {
        invalid = 0;

        printf("\n--- SIGN UP ---");

        printf("\nCreate Username: ");
        scanf("%s", reg_username);

        for (int i = 0; reg_username[i] != '\0'; i++)
        {
            if (reg_username[i] >= '0' && reg_username[i] <= '9')
            {
                printf("Signup failed: invalid username\n");
                invalid = 1;
                break;
            }
        }

        if (invalid)
            continue;

        printf("Create Password: ");
        scanf("%s", reg_password);

        
        for (int i = 0; i < 10; i++)
            number[i] = 0;

        for (int i = 0; reg_password[i] != '\0'; i++)
        {
            if (reg_password[i] >= '0' && reg_password[i] <= '9')
            {
                int num = reg_password[i] - '0';
                if (number[num] == 1)
                {
                    printf("Signup failed: invalid password\n");
                    invalid = 1;
                    break;
                }
                number[num] = 1;
            }
        }

        if (invalid)
            continue;

        printf("Signup successful\n");
        return;
    }
}



int login()
{
  

    printf("\n--- LOGIN ---");
    printf("\nEnter Username: ");
    scanf("%s", &username);

    printf("Enter Password: ");
    scanf("%s", &password);
    printf("please enter email id: ");
    scanf("%s", &email_id);
    printf("please enter mobile number:");
    scanf("%s",&mobile_no);

    if (strcmp(username, "reg_username") == 0 && strcmp(password, "reg_password") == 0)
    {
        printf("\nLogin Successful!");
        return 1;
    }
    else
    {
        return 0;
    }
}

void bookticket()
{

    printf("\n please Enter Bus Number: ");
    scanf("%d", &Bus_number);

    printf("please Enter number of Seats: ");
    scanf("%d", &Seats);
    printf("please Enter your source city: ");
    scanf("%s", &Source_city);
    printf("please Enter your destination city: ");
    scanf("%s", &Destination_city);
    printf("please Enter payment: ");
    scanf("%d", &Payment);
      printf("  ==booking successful.==  \nbus_number:%d \nseats:%d \nsourcecity: %s \ndestinationcity: %s \nPayment :%d", Bus_number, Seats, Source_city, Destination_city, Payment);
            if (Seats <= Total_seats)
            {
               Total_seats = Total_seats - Seats;
               printf("\nBooking Successfully");
               printf("\nAvailable Seats :%d", Total_seats);
            }
            else
            {
               printf("\n not enough  seats available");
            }

}

void cancelticket()
{
   

    printf("\nEnter Ticket Number: ");
    scanf("%d", &Ticket_no);
     printf("please enter number of seats to cancel:");
            scanf("%d", &Seats);
            printf("Cancellation Successful.Bus_number:%d Seats Canceled :%d", Bus_number, Seats);
            Total_seats = Total_seats + Seats;
            printf("\n  Cancellation Successfully  ");
            printf("\n Available Seats Now:%d", Total_seats);

    printf("\nTicket Cancelled Successfully!");
}

void checkstatus()
{
   
    printf("\n****** Check Bus Status ******");
    printf("\nbus number   : %d", Bus_number);
    printf("\n source city   : %s",Source_city);
    printf("\ndestination city : %s",Destination_city);
    printf("\nTotal Seats     : %d", Total_seats);
    printf("Available Seats :%d", Total_seats);
}