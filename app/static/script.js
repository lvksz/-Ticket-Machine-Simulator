document.addEventListener('DOMContentLoaded', function () {
    const ticketTypeSelect = document.getElementById('ticket-type');
    const discountTypeSelect = document.getElementById('discount-type');
    const addButton = document.querySelector('.add-ticket');
    const basket = document.querySelector('.basket-items');
    const totalPriceElement = document.querySelector('.total-price span');
    const payButton = document.querySelector('.button.pay');
    const coinButtons = document.querySelectorAll('.coin');
    
    
    coinButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            const coinValue = parseFloat(button.dataset.value);
            payWithCoin(coinValue);
        });
    });

    function payWithCoin(coinValue) {
        let totalToPayElement = document.querySelector('.total-price span');
        let totalToPay = parseFloat(totalToPayElement.textContent.split(' ')[0]);
    
        if (totalToPay - coinValue <= 0) {
            let overpaid = Math.abs(totalToPay - coinValue);
            if (overpaid > 0) {
                alert(`Reszta: ${overpaid.toFixed(2)} zł`);
            }
            
            clearBasket();
            totalToPayElement.textContent = '0.00 zł';

        } else {
            totalToPay -= coinValue;
            totalToPayElement.textContent = `${totalToPay.toFixed(2)} zł`;
        }
    }

    function clearBasket() {
        basket.innerHTML = '';
    
    }
    function updatePaymentOnServer(coinValue) {
        fetch('/update_payment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ amountPaid: coinValue })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    addButton.addEventListener('click', function (event) {
        event.preventDefault();

        const ticketType = ticketTypeSelect.value;
        const discountType = discountTypeSelect.value;

        fetch('/add_ticket', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ticketType, discountType})
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                addTicketToBasket(data.ticketType, data.discountLabel, data.ticketPrice);
                updateTotalPrice(data.ticketPrice);
            }
        })
        .catch(error => console.error('Error:', error));
    });

    payButton.addEventListener('click', function () {
        const totalAmount = parseFloat(totalPriceElement.textContent.split(' ')[0]);

        fetch('/pay', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({totalAmount})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
                basket.innerHTML = '';
                totalPriceElement.textContent = '0.00 zł';
            } else {
                alert(data.message);
            }
        })
        .catch(error => console.error('Error:', error));
    });

    function addTicketToBasket(ticketType, discountLabel, ticketPrice) {
        const ticketElement = document.createElement('div');
        ticketElement.classList.add('ticket');
    
        const ticketInfo = document.createElement('div');
        ticketInfo.classList.add('ticket-info');
        ticketInfo.textContent = ticketType;
    
        const ticketDiscount = document.createElement('div');
        ticketDiscount.classList.add('ticket-discount');
        ticketDiscount.textContent = discountLabel;
    
        const ticketPriceElement = document.createElement('div');
        ticketPriceElement.classList.add('ticket-price');
        ticketPriceElement.textContent = `${ticketPrice.toFixed(2)} zł`;
    
        const deleteButton = document.createElement('button');
        deleteButton.classList.add('delete-ticket');
    
        const image = document.createElement('img');
        image.src = "../static/images/deleteButton.svg";
        image.alt = "Usuń";
        image.width = 61;
        image.height = 61;
    
        deleteButton.appendChild(image);
    
        deleteButton.addEventListener('click', function() {
            fetch('/remove_ticket', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ticketType, ticketPrice})
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    basket.removeChild(ticketElement);
                    updateTotalPrice(-ticketPrice);
                }
            })
            .catch(error => console.error('Error:', error));
        });

        ticketElement.appendChild(ticketInfo);
        ticketElement.appendChild(ticketDiscount);
        ticketElement.appendChild(ticketPriceElement);
        ticketElement.appendChild(deleteButton);
        
        basket.appendChild(ticketElement);
    }

    function updateTotalPrice(ticketPrice) {
        const currentTotal = parseFloat(totalPriceElement.textContent.split(' ')[0]);
        const newTotal = Math.max(0, currentTotal + ticketPrice);
        totalPriceElement.textContent = `${newTotal.toFixed(2)} zł`;
    }

    function updateDateTime() {
        const now = new Date();
        const dateStr = now.toLocaleDateString('pl-PL', {
            year: 'numeric',
            month: '2-digit',
            day: '2-digit',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: false
        });
        document.querySelector('.date-time').textContent = dateStr;
    }

    setInterval(updateDateTime, 1000);
    updateDateTime();
});
