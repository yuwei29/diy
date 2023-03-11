let f=()=>{
    let t1=Date.now();
    let s=0;
    for(let i=0;i<1000000000;i++){
        s+=i%2;
    }
    let t2=Date.now();
    console.log(t2-t1);
    console.log(s);
}
f();