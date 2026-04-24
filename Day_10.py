import random
import copy
import math
import numpy as np
import pandas as pd

n="Makineni Ruthvik Krishna"
l=len(n)-n.count(" ")

rno=input("Enter Register Number: ")
num=int(rno[-2:])

def gen_data():
    a=[]
    for i in range(15):
        d={
            "zone":i+1,
            "metrics":{
                "traffic":random.randint(10,100),
                "pollution":random.randint(20,300),
                "energy":random.randint(50,500)
            },
            "history":[random.randint(10,100) for _ in range(3)]
        }
        a.append(d)
    return a

def make_copies(a):
    assign=a
    shallow=a[:]
    deep=copy.deepcopy(a)
    return assign,shallow,deep

def mutate(a):
    for i in a:
        i["metrics"]["traffic"]=i["metrics"]["traffic"]+5
        i["history"].append(random.randint(10,100))
        t=i["metrics"]["traffic"]
        p=i["metrics"]["pollution"]
        e=i["metrics"]["energy"]
        i["risk"]=round(math.log(t+p+e) + (l%5),2)
    return a

def personalize(a):
    if num%2==0:
        a.reverse()
    else:
        a=a[3:]+a[:3]
    return a

def to_df(a):
    rows=[]
    for i in a:
        rows.append({
            "zone":i["zone"],
            "traffic":i["metrics"]["traffic"],
            "pollution":i["metrics"]["pollution"],
            "energy":i["metrics"]["energy"],
            "risk":i["risk"]
        })
    return pd.DataFrame(rows)

def analyze(df):
    arr=np.array(df[["traffic","pollution","energy"]])
    mean=np.mean(arr,axis=0)
    var=np.var(arr,axis=0)

    anom=[]
    for i in range(len(df)):
        if df["traffic"][i] > mean[0]+np.std(arr[:,0]):
            anom.append(df["zone"][i])

    t=[]
    p=[]
    for i in range(len(df)):
        t.append(df["traffic"][i])
        p.append(df["pollution"][i])

    mt=sum(t)/len(t)
    mp=sum(p)/len(p)

    nume=0
    den1=0
    den2=0

    for i in range(len(t)):
        nume+=(t[i]-mt)*(p[i]-mp)
        den1+=(t[i]-mt)**2
        den2+=(p[i]-mp)**2

    corr=nume/math.sqrt(den1*den2)

    return mean,var,anom,corr

def patterns(a):
    risks=[i["risk"] for i in a]
    mx=max(risks)
    mn=min(risks)
    stab=1/(np.var(risks)+1)

    high=[i["zone"] for i in a if i["risk"]>5]

    cluster=[]
    for i in range(len(high)-1):
        if high[i+1]==high[i]+1:
            cluster.append(high[i])

    return (mx,mn,round(stab,2)),high,cluster

def decision(avg):
    if avg<4:
        return "System Stable"
    elif avg<5:
        return "Moderate Risk"
    elif avg<6:
        return "High Corruption Risk"
    else:
        return "Critical Failure"

orig=gen_data()
before=copy.deepcopy(orig)

assign,shallow,deep=make_copies(orig)

assign=mutate(assign)
assign=personalize(assign)

print("\n---Before---\n",before[:2])
print("\n---After Assignment---\n",assign[:2])

df=to_df(assign)

mean,var,anom,corr=analyze(df)

tup,high,cluster=patterns(assign)

res=decision(sum(df["risk"])/len(df))

print("\nDataFrame:\n",df.head())

print("\nOriginal vs Deep Same:",before==deep)

print("\nAnomaly Zones:",anom)

print("\nRisk Tuple:",tup)

print("\nHigh Risk Zones:",high)
print("Cluster Zones:",cluster)

print("\nDecision:",res)

if l%2==0:
    print("Observation: Shallow copy affected original due to shared nested objects")
else:
    print("Observation: Deep copy maintained separate structure")

print("\nInsight: Shallow copy corrupts nested structures because inner objects are shared.")