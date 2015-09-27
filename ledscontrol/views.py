from django.shortcuts import render
from django.http import JsonResponse
from ledscontrol.extras import leds


# i2c bus for raspberry pi (model B) on port 1
# from smbus import SMBus
# bus = SMBus(1)

arduinoAddress = 0x12
value = 0b00000
leds = leds.Leds()
leds.asByte = int(value)


def view_test(request):
	return render(request, 'ledscontrol/test.html', {'leds': leds})

def view_update(request):

	# i2c bus for raspberry pi on port 1
	# bus = smbus.SMBus(1)

	data = {}
	data["ref"] = request.POST.get("ref", None)
	data["active"] = request.POST.get("active", None)
	if data["active"] == 'false':
		data["active"] = 0
	else:
		data["active"] = 1
	if data["ref"]:
		setattr(leds, 'led'+data["ref"], int(data["active"]))

	# bus.write_byte(arduinoAddress, leds.asByte)

	data['result'] = 'success'
	data['leds'] = {
		'led1': leds.led1,
		'led2': leds.led2,
		'led3': leds.led3,
		'led4': leds.led4,
		'led5': leds.led5,
	}

	return JsonResponse(data)
