/* var url = 'http://api.exchangeratesapi.io/v1/latest?access_key=56c65b60f1b1854bf84066d5c4095969&format=1'
var currency = null;
async function calculate(){

    const response  = await fetch(url);
    const data = await response.json();

    var currency = $('#currency').val();
    console.log(currency);
    
    


    conversion_rates = (data.rates[currency])
    console.log(conversion_rates)

    document.getElementById('imp').innerHTML =  ' 1 Euro = ' + conversion_rates +' '+ currency +' amount will be divided w.r.t conversion-rate' ; 
    document.getElementById('imp').style.color = 'red';
    
    save_btn = document.getElementById('save')
    save_btn.addEventListener('click',function(){
    amount = document.getElementById('id_income').value;
    console.log(amount)
     
    balance = document.getElementById('id_balance').value;
    console.log(balance)
    
    income_category = document.getElementById('id_income_category').value;
    console.log(income_category)
    if (amount!="")
    {
        
        
        console.log('correct')
        
        console.log(conversion_rates)
        income = (amount/conversion_rates).toFixed(3)
        converted_balance = (balance/conversion_rates).toFixed(3)
        

        fetch("/conversion/",{
            method:'POST',
            headers:{
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,            
        },
        body:JSON.stringify({'conversion_rates':conversion_rates, 'income':income, 'balance':converted_balance,'income_category':income_category}),
      
      
          })
          .then((response) =>{
            return response.json()
        })
         .then((data) =>{
          
             
              console.log('data', data)
              
              
          }) 

        
       
       
        }
        else
        {
        console.log('wrong')
        }
    
    
    }) 


} */


/* save_btn = document.getElementById('set')
save_btn.addEventListener('click',function(){
        calculate();
        console.log('outside',currency);

      
})
 */

var url = 'http://api.exchangeratesapi.io/v1/latest?access_key=56c65b60f1b1854bf84066d5c4095969&format=1'
var currency = null;
async function calculate(){

    const response  = await fetch(url);
    const data = await response.json();

    var currency = $('#currency').val();
    console.log(currency);        
    conversion_rates = (data.rates[currency])
    console.log(conversion_rates)
    
   
    document.getElementById('imp').innerHTML =  ' 1 Euro = ' + conversion_rates +' '+ currency +' amount will be divided w.r.t conversion-rate' ; 
    document.getElementById('imp').style.color = 'red';
    
     
    

};
$( "#currency" ).change(function() {
    
    calculate();

});








   
    
    
    
        
   


 