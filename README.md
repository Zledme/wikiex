# WIKIEX
### To setup the environment
```bash
source setup.sh
```
### To run the server
```bash
uvicorn main:app
```
### For testing
```bash
pytest
```
> [!NOTE]  
> I used linux environment with bash shell, So haven't tested if this will run for windows or other os


### Endpoint
#### 1. topic
    a. This enpoints takes in 2 values:
        1. topic: The topic you want to search
        2. n: number of words
![image](https://github.com/Zledme/wikiex/assets/93548699/b696cce1-159b-47ee-9fb9-a5eb57a67f3a)

    

#### 2. history
    b. return the history in form of list of things searched by the user.
![image](https://github.com/Zledme/wikiex/assets/93548699/4920ddd1-829b-42d3-9c71-31c55bdfcb45)

