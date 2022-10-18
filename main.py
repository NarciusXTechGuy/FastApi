from fastapi import FastAPI


app=FastAPI()

@app.get('/') #@"path operator decorater"."operator"(path or route )
def index(): #path operation function
    return {'data':{'name':'Tenwin'}}

@app.get('/about')
def about():
    return {'data':'about page'}