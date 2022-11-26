window.onload = function() {
    let addComponentFieldBtn = document.getElementById('add_component_button');
    addComponentFieldBtn.addEventListener('click', function(e){
        e.preventDefault();
        let allComponentsFieldWrapper = document.getElementById('sku_components');
        // let allComponentsField = allComponentsFieldWrapper.getElementsByTagName('input');
        // if(allComponentsField.length > 100) {
        //     alert('You can have only 50 components');
        //     return;
        // }
        // let componentInputIds = []
        // for(let i = 0; i < allComponentsField.length; i++) {
        //     componentInputIds.push(parseInt(allComponentsField[i].name.split('-')[1]));
        // }
        // let index = Math.max(...componentInputIds) + 1
        // let newFieldName = `movies-${index}`;
        allComponentsFieldWrapper.insertAdjacentHTML('beforeend',`
        <table id="sku_components-1">
            <tbody>
                <tr>
                    <th>
                        <label for="sku_components-1-component_id">component_id</label>
                    </th>
                    <td>
                        <input id="sku_components-1-component_id" name="sku_components-1-component_id" required="" type="number" value="">
                    </td>
                </tr>
                <tr>
                    <th>
                        <label for="sku_components-1-quantity">quantity</label>
                    </th>
                    <td>
                        <input id="sku_components-1-quantity" name="sku_components-1-quantity" required="" type="text" value="">
                    </td>
                </tr>
            </tbody>
        </table>
        `);
        
        // <li><label for="${newFieldName}">Movie Name</label> <input id="${newFieldName}" name="${newFieldName}" type="text" value=""></li> 
    });
}
