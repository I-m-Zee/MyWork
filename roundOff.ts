    roundOff(value: number, roundTo: number, decimalPlaces: number) {
        let result: number = 0;
        if (roundTo != undefined || decimalPlaces != undefined) {
            let tempVal = this.getDecimalPart(value);
            if (roundTo == 2) { //Lowest
                if (String(tempVal).length > decimalPlaces) {
                    result = Number(`${Math.trunc(value)}.${String(tempVal).slice(0, decimalPlaces)}`)
                } else {
                    result = Number(`${Math.trunc(value)}.${tempVal}`)
                }
            } else if (roundTo == 3) { //Highest
                if (String(tempVal).length > decimalPlaces) {
                    if (Number(String(tempVal).slice(0, decimalPlaces + 1).slice(-1)) > 0) {
                        result = Number(`${Math.trunc(value)}.${Number(String(tempVal).slice(0, decimalPlaces)) + 1}`)
                    } else {
                        result = Number(`${Math.trunc(value)}.${String(tempVal).slice(0, decimalPlaces)}`)
                    }
                } else {
                    result = Number(`${Math.trunc(value)}.${tempVal}`)
                }
            } else {
                //Nearest
                if (decimalPlaces > 0)
                    result = (Math.round(value * Math.pow(10, decimalPlaces)) / Math.pow(10, decimalPlaces));
                else
                    result = (Math.round(value * Math.pow(10, String(tempVal).length)) / Math.pow(10, String(tempVal).length));

            }
        } else {
            //Default
            result = value
        }
        return result
    }

    getDecimalPart(num: number) {
        if (Number.isInteger(num)) {
            return 0;
        }
        const decimalStr = num.toString().split('.')[1];
        return Number(decimalStr);
    }
