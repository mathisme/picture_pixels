view = {
	dimension_text_element : document.getElementById("dim"),
	corners_text_element : document.getElementById("corners"),
	submit_button : document.getElementById("submit"),
	output_paragraph : document.getElementById("output")
};

controller = {
	init : function(){
        view.submit_button.addEventListener("click",this.button_clicked);
    },
	button_clicked : function(){
        const data = {
            "dimensions":view.dimension_text_element.value,
            "corners":view.corners_text_element.value
        }
        const Http = new XMLHttpRequest();
        Http.open("POST","http://127.0.0.1:8000/");
        Http.setRequestHeader("Content-type","application/json;charset=UTF-8");
        Http.send(JSON.stringify(data));
        Http.onreadystatechange = function() {
            if ((this.readyState==4)&&(this.status==200)) {
                view.output_paragraph.textContent = Http.responseText;
            }}
        }
}

controller.init()