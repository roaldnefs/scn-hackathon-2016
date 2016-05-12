<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<title>Bootstrap 101 Template</title>
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.2/css/font-awesome.min.css">
		<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">
		<link rel="stylesheet" href="./assets/style/main.css">
	</head>
	<body>
		<div class="website_wrapper">
			<div class="fluid-container header">
				<div class="container">
					<div class="row desktop_menu">
						<div class="col-xs-12 clearfix">
							<div class="logo pull-left clearfix">
								<span class="fa-stack fa-lg pull-left">
									<i class="fa fa-circle fa-stack-2x"></i>
									<i class="fa fa-btc fa-stack-1x"></i>
								</span>
								<span class="text pull-left">WATCH</span>
							</div>
							<div class="menu pull-right">
								<ul>
									<li><a href="#">HOME</a></li>
									<li><a href="#">PRICEWATCH</a></li>
									<li><a href="#">BEDRIJVEN</a></li>
									<li><a href="#">OVER</a></li>
									<li><a class="btn btn-white" href="#">LOGIN</a></li>
								</ul>
							</div>
						</div>
						<div class="col-xs-12 slogan">
							Ontdek, koop en zoek de beste Bitcoin deals!
						</div>
					</div>
					<div class="row mobile_button">
						<a class="btn btn-white pull-right" href="#">MENU</a>
						<div class="logo pull-left clearfix">
							<span class="fa-stack fa-lg pull-left">
								<i class="fa fa-circle fa-stack-2x"></i>
								<i class="fa fa-btc fa-stack-1x"></i>
							</span>
							<span class="text pull-left">WATCH</span>
						</div>
					</div>
				</div>
			</div>
			<div class="fluid-container mobile_menu">
				<div class="container">
					<div class="row">
						<div class="col-xs-12">
							<ul>
								<li><span style="color: white">></span> <a href="#">HOME</a></li>
								<li><span style="color: white">></span> <a href="#">PRICEWATCH</a></li>
								<li><span style="color: white">></span> <a href="#">BEDRIJVEN</a></li>
								<li><span style="color: white">></span> <a href="#">OVER</a></li>
								<li><span style="color: white">></span> <a href="#">LOGIN</a></li>
							</ul>
						</div>
					</div>
				</div>
			</div>
			
			
			<div class="container main_container">
				<div class="row">
					<div class="col-md-3 content_box filter_menu">
						<div class="box">
							<div class="header"><i class="fa fa-caret-down" aria-hidden="true"></i> Trefwoorden</div>
							<div class="content">
								<form>
									<input type="text" class="form-control input-sm input-trefwoorden" placeholder="Vul trefwoorden in">
								</form>
							</div>
						</div>
						<div class="box">
							<div class="header"><i class="fa fa-caret-down" aria-hidden="true"></i> Prijs</div>
							<div class="content">
								<div id="prijs-slider"></div>
								Prijs range: <span style="font-size: 12px; font-weight: bold;">m</span><i class="fa fa-btc"></i> <input type="text" id="amount" readonly style="border:0; font-weight:bold; width: 50%">
							</div>
						</div>
						<div class="box">
							<div class="header"><i class="fa fa-caret-down" aria-hidden="true"></i> Categorie</div>
							<div class="content">Content</div>
						</div>
						<div class="box">
							<div class="header"><i class="fa fa-caret-down" aria-hidden="true"></i> Bedrijf</div>
							<div class="content">Content</div>
						</div>
						
					</div>
					
					<div class="col-md-8 col-md-offset-1">
						<div class="row product_list">
							<div class="col-xs-12 content_box product clearfix">
								<div class="thumb pull-left"></div>
								
								<div class="content pull-left">
									<div class="title">Een vierkante televisie</div>
									<div class="cat"><i class="fa fa-tag"></i> Televisies</div>
									<div class="desc">Dit is een mooie, maar vierkante TV. Naast een kapot scherm, mist het power knopje ook.</div>
								</div>
								
								<div class="price pull-right">
									<p><span class="btc"><i class="fa fa-btc"></i> 0.00123456</span></p>
									<p><span class="eur"><i class="fa fa-eur"></i> 0.0012</span></p>
									<p><span class="view"><i class="fa fa-eye" aria-hidden="true"></i> 10</p>
								</div>
							</div>
							
							
							
							<div class="col-xs-12 content_box product clearfix">
								<div class="thumb pull-left"></div>
								
								<div class="content pull-left">
									<div class="title">Een vierkante televisie</div>
									<div class="cat"><i class="fa fa-tag"></i> Televisies</div>
									<div class="desc">Dit is een mooie, maar vierkante TV. Naast een kapot scherm, mist het power knopje ook.</div>
								</div>
								
								<div class="price pull-right">
									<p><span class="btc"><i class="fa fa-btc"></i> 0.00123456</span></p>
									<p><span class="eur"><i class="fa fa-eur"></i> 0.0012</span></p>
									<p><span class="view"><i class="fa fa-eye" aria-hidden="true"></i> 10</p>
								</div>
							</div>
							
							
							<div class="col-xs-12 content_box product clearfix">
								<div class="thumb pull-left"></div>
								
								<div class="content pull-left">
									<div class="title">Een vierkante televisie</div>
									<div class="cat"><i class="fa fa-tag"></i> Televisies</div>
									<div class="desc">Dit is een mooie, maar vierkante TV. Naast een kapot scherm, mist het power knopje ook.</div>
								</div>
								
								<div class="price pull-right">
									<p><span class="btc"><i class="fa fa-btc"></i> 0.00123456</span></p>
									<p><span class="eur"><i class="fa fa-eur"></i> 0.0012</span></p>
									<p><span class="view"><i class="fa fa-eye" aria-hidden="true"></i> 10</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		
		<footer class="footer">
			<div class="container">
				<div class="row">
					<div class="col-xs-12">
						Footer!
					</div>
				</div>
			</div>
		</footer>
		
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
		<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
		<script src="./assets/js/product.js"></script>
	</body>
</html>