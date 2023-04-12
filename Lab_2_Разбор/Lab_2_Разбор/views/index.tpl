% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <img src="static\images\logo_nav.png">
    <p></p>
    <p class="lead">Шапка</p>
    <p><a href="http://bottlepy.org/docs/dev/index.html" class="btn btn-primary btn-large">Перейти &raquo;</a></p>
</div>

<div class="row">
    <div class="col-md-4">
        <h2>Проверка - 0</h2>
        <p>
            Описание - 0
        </p>
        <p><a class="btn btn-default" href="http://bottlepy.org/docs/dev/index.html">Перейти &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Проверка - 1</h2>
        <p>Описание - 1</p>
        <p><a class="btn btn-default" href="https://pypi.python.org/pypi">Перейти &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Проверка - 2</h2>
        <p>Описание - 2</p>
        <p><a class="btn btn-default" href="http://azure.microsoft.com">Перейти &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Проверка - 3</h2>
        <p>Описание - 3</p>
        <p><a class="btn btn-default" href="https://translate.google.com/">Перейти &raquo;</a></p>
    </div>
</div>

<h3> Ask a Question </h3>

<form action="/home" method="post">

<p><textarea rows="2" cols="50" name="QUEST" placeholder="Your question"  style = "resize: none";></textarea></p>

<p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>

<p><input type="submit" value="Send"></p>

</form>
