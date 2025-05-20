Roll The Dice Microservice!

Our communication contract:

1. REQUEST data: Package two non-zero positive integers, the first entailing the number, or quantity, of die, and the second integer entails the number of faces, or sides, of each die. Assume all die will share the same number of faces/sides. Enforce data type, i.e. ensure values sending are not <0, or text string. Use JSON package as sending payload, and specify Port to send to. EX: "Input # of die = (get integer value)", "Input # of sides per die = (get integer value)", integer values != (# <0, or 'string') ? then continue, package as JSON file, POST per HTTP protocol to set {PORT #}
2. RECEIVE data: Microservice A will be running on given {PORT #} already by time of call, upon receipt of JSON package data will parse raw data for integer values, use the first for number of die, and the second as the number of sides of each die. Then it will create rolls of each die by using a random number generator from 1 to the number of sides, store this information, and sum up this number for a total. It then packages this response as JSON payload and posts it from the same Port that it is open on. EX: (JSON package of two >0 integers) > parse (JSON package) for #die, #sides, random number generate (1, #sides) x #die -> sum each "roll" (random number generated) -> package rolls and sum, send it via {PORT #}

UML Diagram:
![UML Class Diagram](https://github.com/user-attachments/assets/b6df39c0-a8aa-48ba-a19c-d52f292a1b99)
