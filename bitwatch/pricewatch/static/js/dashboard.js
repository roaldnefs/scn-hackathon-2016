/* Wanneer de DOM geladen is. */
$(document).ready (function ()
{
	/* Wanneer de 'verberg producten' knop ingedrukt wordt. */
	$('.btn-verberg-producten').click (function (e)
	{
		/* Stop standaard klik gedrag. */
		e.preventDefault ();
		
		/* Verander de tekst in de knop. */
		$('.btn-verberg-producten').text ((($('.product_collaps').is (':visible')) ? 'Laat producten zien' : 'Verberg producten'));
		
		/* Toggle de producten lijst. */
		$('.product_collaps').slideToggle ('fast');
	});
});