from fastapi import FastAPI


app=FastAPI()

@app.get('/') #@"path operator decorater"."operator"(path or route )
def index(): #path operation function
    return {'data':{'name':'Tenwin'}}

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get('/blog') #working with the query set eg: /blog?limit=50&published=true
def blog(limit,published):
    if published:
        return {'data':f'{limit} published blogs from db'}
    else:
        return {'data':f'{limit} unpublished blogs from db'}
        


@app.get('blog/unpublished')#string 
def unpublished(): #same name passed in down also only parameters changed one is string and another is integer. line by line execution
    return {'data':'unpublished data'}

@app.get('/blog/{id}') # example /blog/1 or /blog/2 #integer
def show(id:int): # defining type (key:type)
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':[id,'1',id]}


