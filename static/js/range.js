function setVisible(range_box, val) {
    if (val) {
        range_box.style.display = 'block';
    } else {
        range_box.style.display = 'none';
    }
}

function updateRangeValue(element, val) {
    element.textContent = val;
}

function updateCost() {
    const form = document.forms[0];
    let cost = 0;
    for (el of clean_list) {
        if (form.clean_type.value == el.name) {
            cost += el.cost * form[el.name + '_range'].value;
        }
        if (el.group == 'cleanning') {
            if (form[el.name].checked) {
                if (el.is_range) {
                    cost += el.cost * form[el.name + '_range'].value;
                } else {
                    cost += el.cost;
                }
            }
        }
    }
    const costEl = document.getElementById("cost");
    costEl.textContent = cost + " тг.";
}

for (element of clean_list) {

    if (element.is_range) {
        const radio = document.getElementById(element.name);
        const rangeBox = document.getElementById(element.name + "_range_box");
        const range = document.getElementById(element.name + "_range");
        
        setVisible(rangeBox, false);
    
        radio.addEventListener("change", function(e) {
            for (el of clean_list) {
                if (el.is_range) {
                    const radio = document.getElementById(el.name);
                    const rangeBox = document.getElementById(el.name + "_range_box");
                    
                    setVisible(rangeBox, radio.checked);
                }
            }

        }, false);
        
        range.addEventListener("input", function(e) {
            for (el of clean_list) {
                if (el.is_range) {
                    const range = document.getElementById(el.name + "_range");
                    const current_value = document.getElementById(el.name + "_value");
                    
                    if (range == e.target) {
                        updateRangeValue(current_value, e.target.value);
                        updateCost();
                        break;
                    }
                }
            }
        }, false);
        
        range.addEventListener("change", function(e) {
            for (el of clean_list) {
                if (el.is_range) {
                    const range = document.getElementById(element.name + "_range");
                    const current_value = document.getElementById(element.name + "_value");
                    
                    if (range == e.target) {
                        updateRangeValue(current_value, e.target.value);
                        break;
                    }
                }
            }
        }, false); 
    }

    const radio = document.getElementById(element.name);

    radio.addEventListener("click", function(e) {
        updateCost();
    }, false);
}