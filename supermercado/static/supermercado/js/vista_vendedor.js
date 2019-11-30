// creado por matias general
const datos = [];
function agregarProducto(e,form){
    e.preventDefault();
    let datosUsuarios = {};
    datosUsuarios.nombre = form.nombre.value;
    datosUsuarios.precio = form.precio.value;
    datosUsuarios.stock = form.stock.value;
    datosUsuarios.optradio = form.optradio.value;
    datosUsuarios.descripcion = form.descripcion.value;
    datos.push(datosUsuarios);
    listar();
    form.reset();
}


function listar(){
    let tbody = "";
    for(let i=0;i<=datos.length-1;i++){
        let info=datos[i];
        let td = `
            <tr> 
                <td>${info.nombre}</td>
                <td>${info.precio}</td> 
                <td>${info.stock}</td> 
                <td>${info.optradio}</td>
                <td>${info.descripcion}</td>
                <td>
                    <button class="btn btn-danger" onclick="borrarObjeto('${info.nombre}')" >Eliminar</button>
                </td>
                <td>

                </td>
                </tr>
        `
        tbody=tbody + td;
    }
    document.querySelector("#TablaUsuarios tbody").innerHTML = "";
    document.querySelector("#TablaUsuarios tbody").innerHTML = tbody;
}

function desplegar(btn){
    let valorAttr = btn.getAttribute("boton");
    let elemento = document.getElementById(valorAttr);
    let rows = document.getElementsByClassName('row')
    for(let i =0; i<=rows.length-1;i++){
        rows[i].classList.add('esconder')
    
    }
    elemento.classList.remove('esconder');
}

function borrarObjeto(nombre){
    swal.fire({
        title:'Desea borrar este producto',
        text:'Usted borra el producto '+nombre,
        icon:'warning',
        showCancelButton:true
    })
    .then(resultado=>{
        if(resultado.value){
            for(let i=0;i<=datos.length-1;i++){
                if(datos[i].nombre===nombre){
                    datos.splice(i,1);
                    swal.fire({
                        title:'Borrado correctamente',
                        text: `El producto ${nombre} se borro correctamente`,
                        icon:'success'
                    })
                    break;
                }
            }
            listar();
        }else{
            swal.fire({
                text:'Cancelado',
                icon:'info'
            })
        }
    })
}

// function EliminarObjeto(e,form){
//     e.preventDefault();
//     let nombreAEliminar = form.nombreaEliminar.value;
//     for(let i=0;i<=datos.length-1;i++){
//         if(datos[i].nombre===nombreAEliminar){
//             datos.splice(i,1);
//             break;
//         }
//     }
//     listar();
// }

function modificar(e,form){
    e.preventDefault();
    let nombreAmod = form.nombreModificar.value;
    let pos = null;
    let rescatado = {};
    for(let i=0;i<=datos.length-1;i++){
        if(datos[i].nombre === nombreAmod){
            rescatado = datos[i];
            pos = i;
            break;
        }
    }
    form.reset();
    let formMod = document.querySelector("#agregar form");
    let h1 = document.querySelector("#agregar h1");
    h1.textContent = "Modificar";
    formMod.nombre.value = rescatado.nombre;
    formMod.precio.value = rescatado.precio;
    formMod.stock.value= rescatado.stock;
    formMod.optradio.value= rescatado.optradio;
    formMod.descripcion.value = rescatado.descripcion;
    document.getElementById("modificar").classList.add("esconder");
    document.getElementById("agregar").classList.remove("esconder");

    formMod.setAttribute("onsubmit","modificarDatos(event,this,"+pos+")");

}

function modificarDatos(e,form,pos){
    e.preventDefault();
    alert("Producto modificado con éxito");
    let newDatos = {
        nombre:form.nombre.value,
        precio:form.precio.value,
        stock:form.stock.value,
        optradio:form.optradio.value,
        descripcion:form.descripcion.value,
    }
    datos[pos] = newDatos;
    listar();
    formMod.setAttribute("onsubmit","agregarDatos(event,this)");
}
