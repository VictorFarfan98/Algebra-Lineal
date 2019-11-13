from flask import *
from pulp import *
import numpy as np
import matplotlib.pyplot as plt

app = Flask("my app")
print("hello from Docker")


@app.route('/', methods=['GET','POST'])
def whoami():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        #vars, obj, res, signos, op
        Funcion = request.form.getlist("vars")
        obj = request.form.getlist("obj")
        limits = request.form.getlist("limit")
        res = request.form.getlist("res")
        signos = request.form.getlist("signos")
        op = request.form.get("op") #if None: unchecked. 
        print(Funcion)
        print(limits)
        print("res", res)
        print(signos)
        print(op)

        if op == None:
            prob = LpProblem("Ejemplo", LpMinimize)
        else:
            prob = LpProblem("Ejemplo", LpMaximize)
        
        vn = int(len(Funcion))
        rn = int(len(res)/vn)

        print("vn", vn)
        print(rn)


        Variables = []        
        Restricciones = []


        #appending variables
        for i in range(1, vn+1):
            Variables.append(LpVariable(str("Var"+str(i)), 0, None, LpContinuous))

        #Create obj function
        obj = ""
        for i in range(vn):
            obj += "+"+str(Funcion[i])+"*"+"Variables["+str(i)+"]"
        print("obj", obj)

        prob += eval(obj)
        #print(type(res[0]))
        
        #Input de restricciones
        for i in range(rn):
            cur_r = []
            
            print("i", i)
            for j in range(vn):
                #ask = "Ingrese el coeficiente de la restriccion " , str(i+1) , " variable " , Variables[j] ,": "
                print("j", j)

                #cur = input("Ingrese el coeficiente de la restriccion " + str(i+1) + " variable " +str(j+1) + ": ")
                cur = res[int((i*vn)+j)]
                cur_r.append(float(cur))

                
            #signos.append(input("Ingrese el signo de la restriccion (<=, ==, >=): "))
            #limits.append(float(input("Ingrese el valor limite de la restriccion: ")))
            print(cur_r)
            Restricciones.append(cur_r)
        print("res:", Restricciones)
        print("limit:", limits)

        for i in range(len(Restricciones)):
            res = ""
            for j in range(len(Restricciones[i])):
                res += "+ " + str(Restricciones[i][j]) + "*Variables[" + str(j) + "] "
            res += signos[i] + str(limits[i])
            print(res)
            prob += eval(res), "Restriccion" + str(i)

        prob.solve()

        print("Status:", LpStatus[prob.status])
        status = "Status:", LpStatus[prob.status]

        # Each of the variables is printed with it's resolved optimum value

        ans = []
        for v in prob.variables():
            print(v.name, "=", v.varValue)
            ans.append(v.varValue)
        
        total = 0
        for i in range(vn):
            total += float(Funcion[i]) * float(ans[i])


        # Construct lines
        # x > 0
        #x = np.linspace(0, 20, 2000)
        x = np.arange(0, 100, 1)
        # y >= 2
        y1 = (x*0) + 2
        # 2y <= 25 - x
        y2 = (25-x)/2.0
        # 4y >= 2x - 8 
        y3 = (2*x-8)/4.0
        # y <= 2x - 5 
        y4 = 2 * x -5

        plt.figure()
        for i in range(rn):
            #y = Funcion[0]*x + Funcion[1]/ 
            #y = (float(Restricciones[i][0])*x + float(Restricciones[i][1])) / float(limits[i])
            y = []
            for j in range(100):
                y.append((float(limits[i]) - float(Restricciones[i][0])) / float(Restricciones[i][1]))
            #y = (float(limits[i]) - float(Restricciones[i][0])) / float(Restricciones[i][1])
            plt.plot(x, y, label=i)

        # Make plot
        
        #plt.plot(x, y2, label=r'$2y\leq25-x$')
        #plt.plot(x, y3, label=r'$4y\geq 2x - 8$')
        #plt.plot(x, y4, label=r'$y\leq 2x-5$')
        #plt.xlim((0, 16))
        #plt.ylim((0, 11))
        plt.xlabel(r'$x$')
        plt.ylabel(r'$y$')

        # Fill feasible region
        #y5 = np.minimum(y2, y4)
        #y6 = np.maximum(y1, y3)
        #plt.fill_between(x, y5, y6, where=y5>y6, color='grey', alpha=0.5)
        #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        plt.savefig('./static/area.png')


        return render_template('index.html', status=status, ans=ans, total=total)
    else:
        return "Invalid Method"

@app.route('/multi', methods=['GET', 'POST'])
def victor():
    if request.method == "GET":
        return render_template('multi.html')
    elif request.method == "POST":
        #vars, obj, res, signos, op
        Funcion = request.form.getlist("vars")
        obj = request.form.getlist("obj")
        limits = request.form.getlist("limit")
        res = request.form.getlist("res")
        signos = request.form.getlist("signos")
        op = request.form.get("op") #if None: unchecked. 
        print(Funcion)
        print(limits)
        print("res", res)
        print(signos)
        print(op)

        if op == None:
            prob = LpProblem("Ejemplo", LpMinimize)
        else:
            prob = LpProblem("Ejemplo", LpMaximize)
        
        vn = int(len(Funcion))
        rn = int(len(res)/vn)

        print("vn", vn)
        print(rn)


        Variables = []        
        Restricciones = []


        #appending variables
        for i in range(1, vn+1):
            Variables.append(LpVariable(str("Var"+str(i)), 0, None, LpContinuous))

        #Create obj function
        obj = ""
        for i in range(vn):
            obj += "+"+str(Funcion[i])+"*"+"Variables["+str(i)+"]"
        print("obj", obj)

        prob += eval(obj)
        #print(type(res[0]))
        
        #Input de restricciones
        for i in range(rn):
            cur_r = []
            
            print("i", i)
            for j in range(vn):
                #ask = "Ingrese el coeficiente de la restriccion " , str(i+1) , " variable " , Variables[j] ,": "
                print("j", j)

                #cur = input("Ingrese el coeficiente de la restriccion " + str(i+1) + " variable " +str(j+1) + ": ")
                cur = res[int((i*vn)+j)]
                cur_r.append(float(cur))

                
            #signos.append(input("Ingrese el signo de la restriccion (<=, ==, >=): "))
            #limits.append(float(input("Ingrese el valor limite de la restriccion: ")))
            print(cur_r)
            Restricciones.append(cur_r)
        print("res:", Restricciones)
        print("limit:", limits)

        for i in range(len(Restricciones)):
            res = ""
            for j in range(len(Restricciones[i])):
                res += "+ " + str(Restricciones[i][j]) + "*Variables[" + str(j) + "] "
            print(i)
            res += signos[i] + str(limits[i])
            print(res)
            prob += eval(res), "Restriccion" + str(i)

        prob.solve()

        print("Status:", LpStatus[prob.status])
        status = "Status:", LpStatus[prob.status]

        # Each of the variables is printed with it's resolved optimum value

        ans = []
        for v in prob.variables():
            print(v.name, "=", v.varValue)
            ans.append(v.varValue)
        
        total = 0
        for i in range(vn):
            total += float(Funcion[i]) * float(ans[i])

        return render_template('multi.html', status=status, ans=ans, total=total)
    else:
        return "Invalid Method"
    
app.run(host="0.0.0.0", port=5000)

