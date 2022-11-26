$(document).ready(function() {
    var MaxInputs       = 50; //maximum input boxes allowed
    var InputsWrapper   = $("#components_wrapper"); //Input boxes wrapper ID
    var AddButton       = $("#add_component_button"); //Add button ID
      
    var x = InputsWrapper.length; //initlal text box count
    var FieldCount=1; //to keep track of text box added
      
    $(AddButton).click(function (e)  //on add input button click
    {
            if(x <= MaxInputs) //max input box allowed
            {
                FieldCount++; //text box added increment
                //add input box
                $(InputsWrapper).append(`
                                        <div class="row">
                                        <li>
                                            <label for="sku_components-` + x + `">Sku Components-` + x + `</label> 
                                            <table id="sku_components-` + x + `">
                                                <tbody>
                                                    <tr>
                                                        <th>
                                                            <label for="sku_components-` + x + `-component_id">component_id</label>
                                                        </th>
                                                        <td>
                                                            <input id="sku_components-` + x + `-component_id" name="sku_components-` + x + `-component_id" required="" type="number" value="">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th>
                                                            <label for="sku_components-` + x + `-quantity">quantity</label>
                                                        </th>
                                                        <td>
                                                            <input id="sku_components-` + x + `-quantity" name="sku_components-` + x + `-quantity" required="" type="text" value="">
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </li>
                                        <a href="#" class="btn btn-danger removeclass">×</a>
                                        </div>
                                        `);

                x++; //text box increment
            }
    return false;
    });
      
    $("body").on("click",".removeclass", function(e){ //user click on remove text
            if( x > 1 ) {
                    $(this).parent('div').remove(); //remove text box
                    x--; //decrement textbox
            }
    return false;
    })
     $('#submit').click(function(){            
               $.ajax({  
                    url:"/postskill",  
                    method:"POST",  
                    data:$('#add_skills').serialize(),  
                    success:function(data)  
                    {  alert(data)
                         $('#resultbox').html(data);  
                         $('#add_skills')[0].reset();  
                    }  
               });  
          }); 
});