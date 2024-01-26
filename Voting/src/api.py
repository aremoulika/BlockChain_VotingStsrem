from flask import Flask,request
from ledger import castvote,result


app=Flask(__name__)

@app.route('/castvote',methods=['get'])
def castvote1():
    wallet=request.args.get('wallet')
    id=request.args.get('id')
    id1=int(id)
    print(wallet,id,type(id1))
    response=castvote(wallet,id1)
    return {'response':response}

@app.route('/result',methods=['get'])
def result1():
    wallet=request.args.get('wallet')
    print(wallet)
    response=result(wallet)
    return {'response':response}

if __name__=="__main__":
    app.run(
        host='0.0.0.0',
        port='3000',
        debug=True
    )