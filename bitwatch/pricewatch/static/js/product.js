/* Een array waar alle producten in komen die gebuild moeten worden. */
var build_array_data = new Array ();

/* Timeouts defineren. */
var timeout_trefwoorden;

/* Prijs range defineren. */
var price_range = {low: 1, high: 1000};

/* Zoek woorden. */
var zoekwoorden = undefined;

/* Producten object. */
var product_data;

/* Betaalde producten. */
var product_special;

/* Plek om aan te geven hoeveel items er al geladen zijn. */
var current_build_iterator = 0;

/* Hoeveel items laden per keer? */
var iterator_load_each_time = 7;


/* Wanneer de DOM (dus niet eventuele plaatjes) geladen is. */
$(document).ready (function ()
{
	/* Maak een 'in_array' fuctie, en voeg deze toe aan de Array als prototype. */
	Array.prototype.in_array = function (needle)
	{
		/* Return var. */
		var return_var = false;

			/* Doorloop de array. */
			$.each (this, function (i, value)
			{
				/* Is de value de needle? */
				if (value == needle)
				{
					/* Geef aan dat we een match hebben. */
					return_var = true;

					/* Ja! return true. */
					return false;
				}
			});

		/* Geen true gereturned, dus return false. */
		return return_var;
	};


	Array.prototype.filter = function (id)
	{
		/* Heeft deze array inhoud? */
		if (this.length != 0)
		{
			/* Ja. Bevat het array dit ID? */
			if (!this.in_array (id))
			{
				/* Nee, dus return een false. */
				return false;
			}
		}

		/* Return een true. */
		return true;
	}


	/* Functie om te controleren of de opgegeven prijs binnen de geselecteerde range valt. */
	function price_in_range (input)
	{
		/* Is de low range 1, en is de input 1 of lager? */
		if (price_range.low == 1 && input <= 1)
		{
			/* Return dan true. */
			return true;
		}

		/* Zelfde voor high. */
		if (price_range.high == 1000 && input >= 1000)
		{
			/* Return true. */
			return true;
		}

		/* Valt de prijs binnen de opgegeven data? */
		if (input >= price_range.low && input <= price_range.high)
		{
			/* Ja, return true. */
			return true;
		}

		/* Geen 1 van de condities gelden. Return false. */
		return false;
	}


	/* Functie om te controleren of een woorden array voorkomt in een string. */
	function word_in_string (data, trefwoorden)
	{
		/* Zijn er trefwoorden? */
		if (trefwoorden === undefined)
		{
			/* Nee, dus return true, omdat er veder niks gefilterd hoeft te worden. */
			return true;
		}

		/* Maak een return array aan. */
		var return_data = false;

		/* Lower string de data. */
		data = data.toLowerCase ();

		/* Sloop de trefwoorden uit elkaar op spaties. */
		trefwoorden_split = trefwoorden.split (' ');

			/* Doorloop nu elk item. */
			$.each (trefwoorden_split, function (i, item)
			{
				/* Bestaat dit woord in de data string? */
				if (data.indexOf (item.toLowerCase ()) >= 0)
				{
					/* Zet de return data op true. */
					return_data = true;

					/* Break de loop. */
					return false;
				}
			});

		/* Return de return_data. */
		return return_data;
	}
	
	
	/* Functie om het aantal BTC te berekenen van de prijs + de koers. */
	function get_btc_by_eur (euro)
	{
		/* Return het BTC bedrag. */
		var btc = ((euro / 100) / exchage_bitcoin)
		
		/* Bereken 10 ^ 6. */
		var t = Math.pow (10, 6);
		
		/* Return het geheel afgerond op 6 dec. */
		return (Math.round (btc * t) / t).toFixed (6); 
	}
	

	/* Functie om een categorie naam op te halen. */
	function get_cat_by_id (id)
	{
		/* Pak de naam van de categorie. */
		var cat = $('input[name="filter_categorie[]"][value="' + id + '"]').parent ().text ();

			/* Bestaat de cat? */
			if (cat !== undefined)
			{
				/* Ja, dus return deze. */
				return cat;
			}
			else
			{
				/* Nee, dus return 'onbekend'. */
				return 'Onbekend';
			}
	}


	/* Functie om de build_array te (re)builden. */
	function build ()
	{
		/* Is er data? */
		if (build_array_data.length != 0)
		{
			/* Een tijdelijke array aanmaken. */
			var temp = {special: [], normal: []};
			
				/* Doorloop de gehele build array data. */
				$.each (build_array_data, function (i, obj)
				{
					/* Is dit obj. een speciale object? */
					if (product_special.in_array (obj.pk))
					{
						/* Geef aan dat het een special object is. */
						obj.special = true;
						
						/* Knal het object in de special temp. array. */
						temp.special.push (obj);
					}
					else
					{
						/* Geef aan dat het geen special object is. */
						obj.special = false;
						
						/* Knal het object in de normale temp. array. */
						temp.normal.push (obj);
					}
				});
			
			/* Merge de arrays, zodat de special items bovenaan staan en de normal erna. */
			var merged = $.merge (temp.special, temp.normal);
			
				/* Is de huidige iterato + het aantal items wat geladen moet worden hoger dan wat de merged array aan items heeft? */
				if ((current_build_iterator + iterator_load_each_time) > merged.length)
				{
					/* Ja, dus geef de max lengte, het zelfde lengte als de merged array is. */
					var temp_i = merged.length;
				}
				else
				{
					/* Nee, dus pak het huidige iterato, en tel hier het aantal bij op wat per keer geladen meot worden. */
					var temp_i = (current_build_iterator + iterator_load_each_time);
				}
				
				/* Doorloop nu net zovaak, als het aantal items wat weergeven moet worden. */
				for (var i = current_build_iterator; i < temp_i; i++)
				{
					/* Defineer het object. */
					var obj = merged[current_build_iterator];
					
					/* Maak een html var aan. */
					var html = '<div class="col-xs-12 content_box ' + ((obj.special) ? 'product_yellow' : '') + ' clearfix">';
						html += '<div class="thumb pull-left" style="background-image: url(\'' + obj.fields.image + '\'); background-size: cover;"></div>';
						html += '<div class="content pull-left">';
							html += '<div class="title"><a href="/product/' + obj.fields.slug + ' ">' + obj.fields.name + '</a></div>';
							html += '<div class="cat"><i class="fa fa-tag"></i> ' + get_cat_by_id (obj.fields.category) + '</div>';
							html += '<div class="desc">' + obj.fields.description + '</div>';
						html += '</div>';
						html += '<div class="inner-fade"></div>';
						html += '<div class="price pull-right">';
							html += '<p><span class="btc"><i class="fa fa-btc"></i> ' + get_btc_by_eur (obj.fields.price) + '</span></p>';
							html += '<p><span class="eur"><i class="fa fa-eur"></i> ' + (obj.fields.price / 100) + '</span></p>';
							html += '<p><span class="view"><i class="fa fa-eye" aria-hidden="true"></i> ' + obj.fields.views + '</p>';
						html += '</div>';
					html += '</div>';
				
					/* Voeg vervolgens dit element toe aan de container. */
					$('.product_list').append (html);
					
					/* Tel 1 bij de huidige iterator op voor de volgende run in de loop. */
					current_build_iterator++;
				}
		}
		else
		{
			/* Bestaat de 'geen producten' melding al? */
			if ($('.no-products').length == 0)
			{
				/* Er zijn geen resultaten gevonden. */
				$('.product_list').append ('<div class="col-xs-12 content_box product clearfix no-products" style="color: gray; font-style: italic; text-align: center; padding-top: 40px;">Er zijn geen resultaten gevonden.</div>');
			}
		}
	}


	/* Functie om de build_array te bouwen aan de hand van de ingestelde filters. */
	function build_array ()
	{
		/* Maak een filter array aan. */
		var filter = {categorie: [], company: []};

		/* Leeg de build_array_data array. */
		build_array_data = new Array ();

		/* Doorloop alle categorieën. */
		$('input[name="filter_categorie[]"]').each (function ()
		{
			/* Is de huidige checkbox gechecked? */
			if (this.checked)
			{
				/* Ja, dus zet het ID in de filter array. */
				filter.categorie.push (parseInt ($(this).val ()));
			}
		});


		/* Doe dit zelfde bij de bedrijven. */
		$('input[name="filter_company[]"]').each (function ()
		{
			/* Is de huidige checkbox gechecked? */
			if (this.checked)
			{
				/* Ja, dus zet het ID in de filter array. */
				filter.company.push (parseInt ($(this).val ()));
			}
		});


		/* Doorloop door de product_data array. */
		$.each (product_data, function (key, obj)
		{
			/* Voeldoet dit item aan de zoek resultaten? */
			if (filter.categorie.filter (obj.fields.category) && filter.company.filter (obj.fields.company) && price_in_range (parseFloat (obj.fields.price * 1000)) && (word_in_string (obj.fields.name, zoekwoorden) || word_in_string (obj.fields.description, zoekwoorden)))
			{
				/* Voeg het item toe aan de build array. */
				build_array_data.push (obj);
			}

		});

		/* Leeg de product array. */
		$('.product_list').html ('');
		
		/* Knal de iterator op 0. */
		current_build_iterator = 0;
		
		/* Bouw de array op. */
		build ();
	}
	
	
	/* Wanneer er gescrolled wordt in het document. */
	$(window).scroll (function ()
	{
		/* Is het beeld 100px van de bodem verwijderd? */
		if ($(window).scrollTop () + $(window).height () > $(document).height () - 100)
		{
			/* Ja! Dus laad de volgende items in. */
			build ();
		}
	});
	
	
	

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
			/* Is er zoek resultaat? */
			if ($(that).val ())
			{
				/* Sla de zoek woorden op. */
				zoekwoorden = $(that).val ();
			}
			else
			{
				/* Geen resultaat, dus maak undefined. */
				zoekwoorden = undefined;
			}

            /* Roep de build array aan. */
			build_array ();
        }, 100);
    });


	/* Wanneer een categorie geselecteerd wordt. */
	$('input[name="filter_categorie[]"]').change (function ()
	{
		/* Roep de build array aan. */
		build_array ();
    });


	/* Wanneer een categorie geselecteerd wordt. */
	$('input[name="filter_company[]"]').change (function ()
	{
		/* Roep de build array aan. */
		build_array ();
	});
	
	
	/* Wanneer de euro vulta wordt getoggled. */
	$('input[name="filter_vulta[]"]').change (function ()
	{
		/* Gaat het om euro? */
		if ($(this).val() == 'show_euro')
		{
			/* Is de box gechecked? */
			if ($(this).is (':checked'))
			{
				/* Ja, dus laat alles zien. */
				$('.product_list .eur').show ();
			}
			else
			{
				/* Nee, dus verberg alles. */
				$('.product_list .eur').hide ();
			}
		}
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
        values: [1, 1000],

        /* Wanner er geslide wordt. */
        slide: function (event, ui)
        {
			/* Sla de max prijs op. */
			price_range.high = ui.values[1];

			/* Sla de min prijs op. */
			price_range.low = ui.values[0];

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

			/* Roep de build array aan. */
			build_array ();
        }
    });

	/* Laat de nieuwe waardes in de filter bar zien. */
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


	/* Parse de producten (JSON formaat) naar een object. */
	product_data = ((typeof (product_json) !== 'undefined') ? jQuery.parseJSON (product_json) : '');
	
	/* Parse de speciale producten. */
	product_special = ((typeof (advertisements_json) !== 'undefined') ? jQuery.parseJSON (advertisements_json) : '');
	
		/* Is er data? */
		if (product_data != '')
		{
			/* En build daarna de initiele data. */
			build_array ();
		}
});
