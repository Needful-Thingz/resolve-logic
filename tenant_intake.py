<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tenant Maintenance Intake - Resolve</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 flex items-center justify-center h-screen">

<div class="max-w-md w-full bg-white p-8 rounded-lg shadow-md text-center" id="step-1">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">HVAC Diagnostic</h1>
    <p class="text-gray-600 mb-6">Is there a build-up of ice on the copper pipes at the outside AC unit (condenser)?</p>
    <button class="w-full bg-blue-600 text-white font-bold py-3 rounded mb-3 hover:bg-blue-700" onclick="handleIce('yes')">Yes, there is ice</button>
    <button class="w-full bg-gray-200 text-gray-800 font-bold py-3 rounded hover:bg-gray-300" onclick="handleIce('no')">No, there is no ice</button>
</div>

<div class="max-w-md w-full bg-white p-8 rounded-lg shadow-md text-center hidden" id="step-2">
    <h1 class="text-2xl font-bold text-gray-800 mb-4">Fan Diagnostic</h1>
    <p class="text-gray-600 mb-6">Listen to the outside AC unit, then check the vents inside. Which fans are running?</p>
    <button class="w-full bg-blue-600 text-white font-bold py-3 rounded mb-3 hover:bg-blue-700" onclick="handleFans('both')">Both fans are running</button>
    <button class="w-full bg-blue-600 text-white font-bold py-3 rounded mb-3 hover:bg-blue-700" onclick="handleFans('inside')">ONLY the inside fan is running</button>
    <button class="w-full bg-blue-600 text-white font-bold py-3 rounded mb-3 hover:bg-blue-700" onclick="handleFans('outside')">ONLY the outside fan is running</button>
    <button class="w-full bg-blue-600 text-white font-bold py-3 rounded hover:bg-blue-700" onclick="handleFans('neither')">Neither fan is running</button>
</div>

<div class="max-w-md w-full bg-white p-8 rounded-lg shadow-md text-center hidden" id="action-screen">
    <h1 class="text-2xl font-bold text-red-600 mb-4">Mandatory Action Required</h1>
    <p id="action-text" class="text-gray-700 font-medium mb-6 text-left"></p>
    <button class="w-full bg-green-600 text-white font-bold py-3 rounded hover:bg-green-700 hidden" id="submit-btn" onclick="submitTicket()">Submit Ticket to Maintenance</button>
</div>

<div class="max-w-md w-full bg-white p-8 rounded-lg shadow-md text-center hidden" id="success-screen">
    <h1 class="text-3xl font-bold text-green-600 mb-4">✓ Ticket Submitted</h1>
    <p class="text-gray-600">Your diagnostic data has been routed to the maintenance supervisor.</p>
</div>

<script>
    let diagnosticData = { issue: 'HVAC - No Cool', details: '', urgency: '' };

    function handleIce(answer) {
        if (answer === 'yes') {
            diagnosticData.details = 'System Frozen. Instructed to turn off AC and turn FAN ON to thaw.';
            diagnosticData.urgency = 'High';
            showAction('Please turn your thermostat to the OFF position, and turn the FAN setting to ON. This will thaw the ice. A technician cannot work on a frozen unit.', true);
        } else {
            document.getElementById('step-1').classList.add('hidden');
            document.getElementById('step-2').classList.remove('hidden');
        }
    }

    function handleFans(answer) {
        document.getElementById('step-2').classList.add('hidden');
        if (answer === 'both') {
            diagnosticData.details = 'Both fans running but no cool. Instructed to check air filter.';
            diagnosticData.urgency = 'Routine';
            showAction('Please check your indoor air filter. A clogged filter restricts airflow and stops cooling. If the filter is clean, submit a ticket below.', true);
        } else if (answer === 'inside') {
            diagnosticData.details = 'Condenser dead, blower running. High probability of bad capacitor or dirty coils. Instructed to turn system OFF.';
            diagnosticData.urgency = 'High';
            showAction('CRITICAL: Turn your thermostat to the OFF position immediately. Leaving it running will permanently damage the outside compressor.', true);
        } else if (answer === 'outside') {
            diagnosticData.details = 'Blower dead, condenser running. High probability of frozen coils. Instructed to turn system OFF.';
            diagnosticData.urgency = 'High';
            showAction('CRITICAL: Turn your thermostat to the OFF position immediately. The system will freeze into a block of ice if left running.', true);
        } else if (answer === 'neither') {
            diagnosticData.details = 'Total power loss (Thermostat blank / Neither fan running). Instructed to check breakers and float switch.';
            diagnosticData.urgency = 'Routine';
            showAction('<strong>Please check the following before submitting a ticket:</strong><br><br>1. Check the thermostat batteries (if applicable).<br>2. Check your indoor electrical panel for a tripped AC breaker.<br>3. Check the drain pan/float switch at your indoor air handler for standing water.<br><br>If all three are clear and the system is still dead, submit a ticket below.', true);
        }
    }

    function showAction(text, showSubmit) {
        document.getElementById('action-text').innerHTML = text;
        document.getElementById('action-screen').classList.remove('hidden');
        if (showSubmit) {
            document.getElementById('submit-btn').classList.remove('hidden');
        }
    }

    function submitTicket() {
        const ticketId = '#RES-' + Math.floor(1000 + Math.random() * 9000);
        
        const newTicket = {
            id: ticketId,
            property: 'Pending Assignment',
            issue: diagnosticData.issue,
            diagnosis: diagnosticData.details,
            urgency: diagnosticData.urgency
        };
        
        let tickets = JSON.parse(localStorage.getItem('resolveTickets')) || [];
        tickets.push(newTicket);
        localStorage.setItem('resolveTickets', JSON.stringify(tickets));

        document.getElementById('action-screen').classList.add('hidden');
        document.getElementById('success-screen').classList.remove('hidden');
    }
</script>

</body>
</html>
