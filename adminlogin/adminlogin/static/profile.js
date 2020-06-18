function deleteuser(userid){

    
    data = {'userid':userid}
    $.ajax({
        type: 'POST',
        url: '../deleteuser' + '/',
        data: JSON.stringify(data),
        contentType:"application/json",
        dataType: "json",
        headers:{
            "X-CSRFToken":$("input[name=csrfmiddlewaretoken]").val()
        }
    }).done(function (data) {
        
        if (data.deleted == true){
    successpop('User deleted successfully!','error')
    location.reload();

        }
        else{
    successpop('Some error occurred!','error')

        }

    });

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
