function signup(){
  
    username = document.getElementsByName('username')[0].value
    password =document.getElementsByName('psw')[0].value
    cpassword = document.getElementsByName('psw-repeat')[0].value

    

    if (username.length==0 || password.length ==0 || cpassword.length == 0){
        successpop('Please enter all details','error')
    }
    else if(password != cpassword && username.length!=0 && password.length!=0 && cpassword.length!=0){

        successpop('Please enter same password in both fields!','error')

    }
    else if(users.includes(username) == true){

        successpop('This username is already taken.Please select any other username!','error')


    }
    else{
        
        data = {'username':username,'password':password}
        $.ajax({
            type: 'POST',
            url: '',
            data: JSON.stringify(data),
            contentType:"application/json",
            dataType: "json",
            headers:{
                "X-CSRFToken":$("input[name=csrfmiddlewaretoken]").val()
            }
        }).done(function (data) {
            
            if (data.createduser == true){
        successpop('User added successfully! You can now login.','success')
        window.location.href = '../'
    
            }
            else{
        successpop('Some error occurred.Please try again!','error')
    
            }
    
        });
    
    }
    
    }


function successpop(msg, icon){
    Swal.fire({
        position: 'center',
        icon: icon,
        width: 500,
        title: msg,
        
        showConfirmButton: false,
        timer: 3000
    })

    
}