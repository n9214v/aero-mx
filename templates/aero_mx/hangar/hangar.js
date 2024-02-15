/**
function get_aircraft_categories(){
    $.ajax({
        type:   "GET",
        url:    "{#url 'hangar:ajax_aircraft_categories'#}",
        data:   { ts: new Date().getTime() },
        beforeSend:function(){

        },
        success:function(categories){

        },
        error:function(){},
        complete:function(){
        }
    });
   };
}
**/