function reload ()
{

}


/* Trefwoorden timeout. */
var timeout_trefwoorden;


$(document).ready (function ()
{

    /* Wanneer er op de mobiel knop gedrukt wordt. */
    $('.mobile_button').click (function (e)
    {
        /* Negeer default klik gedrag. */
        e.preventDefault ();

        /* Toggle het mobiele menu. */
        $('.mobile_menu').slideToggle ('fast');
    });


    /* Wanneer het scherm geresized wordt. */
    $(window).resize (function ()
    {
        /* Is de width breeder dan 767px? */
        if ($(window).width () > 767)
        {
            /* Is het mobiele menu aanwezig? */
            if ($('.mobile_menu').is (':visible'))
            {
                /* Ja, dus slide hem dicht. */
                $('.mobile_menu').slideUp ('fast');
            }
        }
    });


    /* Wanneer de trefwoorden aangepast worden. */
    $('.input-trefwoorden').on ('input', function (e)
    {
        /* Clear de timeout. */
        clearTimeout (timeout_trefwoorden);

        /* Maak 'this' bruikbaar binnen de timeout. */
        var that = this;

        /* Set een nieuwe timeout. */
        timeout_trefwoorden = setTimeout (function ()
        {
            /* Debug. */
            console.log ("Trefwoorden: " + $(that).val ());
        }, 400);
    });


    /* Maak van de prijs slider een slider object. */
    $("#prijs-slider").slider ({
        /* Het is een range (2 inputs). */
        range: true,

        /* Min. value is 1. */
        min: 1,

        /* Max. value is 1000. */
        max: 1000,

        /* Value range is 1 tot en met 100. */
        values: [1, 100],

        /* Wanner er geslide wordt. */
        slide: function (event, ui)
        {
            /* Is het eerste value een 1? */
            if (ui.values[0] == 1)
            {
                /* Ja, zet er een < teken voor. */
                ui.values[0] = '< ' + ui.values[0];
            }

            /* Is de laatste value hoger dan 1000? */
            if (ui.values[1] == 1000)
            {
                /* Ja, zet er een > teken voor. */
                ui.values[1] = ui.values[1] + ' >';
            }

            /* Vul de waardes is de input in. */
            $('#amount').val (ui.values[0] + ' tot ' + ui.values[1]);
        }
    });

    $('#amount').val (' < ' + $('#prijs-slider').slider ('values', 0) + ' tot ' + $('#prijs-slider').slider ('values', 1));


    /* Wanneer er over een product heen gehoverd wordt. */
    $('.product').hover (
        /* Wanneer muis erop gezet wordt. */
        function ()
        {
            /* Stop alle overige animaties, en geef alle andere producten (op die gene waar de muis op zit na) opacity 0.6 in 150ms. */
            $('.product').not (this).stop ().animate ({opacity: 0.6}, 150);
        },
        function ()
        {
            /* Stop alle overige animaties, en geef alle andere producten (op die gene waar de muis op zit na) opacity 1 in 150ms. */
            $('.product').not (this).stop ().animate ({opacity: 1}, 150);
        }
    );


    /* Wanneer er op een title in de filter box geklikt wordt. */
    $('.filter_menu .box .header').click (function ()
    {
        /* Haal de header en content element op. */
        var header = $(this).parent().find ('.header');
        var content = $(this).parent().find ('.content');

            /* Is de content zichtbaar? */
            if (content.is (':visible'))
            {
                /* Ja, dus verberg deze, vervang de fa caret icon en maak de tekst grijs. */
                $(header).find ('i').removeClass ('fa-caret-down').addClass ('fa-caret-up').parent ().css ('color', 'gray');
            }
            else
            {
                /* Nee, dus laat deze zien, vervang de fa caret icon en maak de tekst weer zwart. */
                $(header).find ('i').removeClass ('fa-caret-up').addClass ('fa-caret-down').parent ().css ('color', 'inherit');
            }

        /* Toggel de zichtbaarheid van de content, en stop de al lopende toggle als die aanwezig is. */
        content.stop ().slideToggle ('fast');
    });
});
