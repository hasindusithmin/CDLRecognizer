
html = '''
<section id="main_content" class="inner">
<h1>Pattern Recognition Functions</h1>
<h3>CDL2CROWS - Two Crows</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDL2CROWS</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDL3BLACKCROWS - Three Black Crows</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDL3BLACKCROWS</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDL3INSIDE - Three Inside Up/Down</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDL3INSIDE</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDL3LINESTRIKE - Three-Line Strike</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDL3LINESTRIKE</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDL3OUTSIDE - Three Outside Up/Down</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDL3OUTSIDE</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDL3STARSINSOUTH - Three Stars In The South</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDL3STARSINSOUTH</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDL3WHITESOLDIERS - Three Advancing White Soldiers</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDL3WHITESOLDIERS</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLABANDONEDBABY - Abandoned Baby</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLABANDONEDBABY</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">,</span> <span class="highlight n">penetration</span><span class="highlight o">=</span><span class="highlight mi">0</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLADVANCEBLOCK - Advance Block</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLADVANCEBLOCK</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLBELTHOLD - Belt-hold</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLBELTHOLD</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLBREAKAWAY - Breakaway</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLBREAKAWAY</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLCLOSINGMARUBOZU - Closing Marubozu</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLCLOSINGMARUBOZU</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLCONCEALBABYSWALL - Concealing Baby Swallow</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLCONCEALBABYSWALL</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLCOUNTERATTACK - Counterattack</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLCOUNTERATTACK</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLDARKCLOUDCOVER - Dark Cloud Cover</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLDARKCLOUDCOVER</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">,</span> <span class="highlight n">penetration</span><span class="highlight o">=</span><span class="highlight mi">0</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLDOJI - Doji</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLDOJI</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLDOJISTAR - Doji Star</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLDOJISTAR</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLDRAGONFLYDOJI - Dragonfly Doji</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLDRAGONFLYDOJI</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLENGULFING - Engulfing Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLENGULFING</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLEVENINGDOJISTAR - Evening Doji Star</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLEVENINGDOJISTAR</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">,</span> <span class="highlight n">penetration</span><span class="highlight o">=</span><span class="highlight mi">0</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLEVENINGSTAR - Evening Star</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLEVENINGSTAR</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">,</span> <span class="highlight n">penetration</span><span class="highlight o">=</span><span class="highlight mi">0</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLGAPSIDESIDEWHITE</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLGRAVESTONEDOJI - Gravestone Doji</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLGRAVESTONEDOJI</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLHAMMER - Hammer</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLHAMMER</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLHANGINGMAN - Hanging Man</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLHANGINGMAN</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLHARAMI - Harami Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLHARAMI</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLHARAMICROSS - Harami Cross Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLHARAMICROSS</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLHIGHWAVE - High-Wave Candle</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLHIGHWAVE</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLHIKKAKE - Hikkake Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLHIKKAKE</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLHIKKAKEMOD - Modified Hikkake Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLHIKKAKEMOD</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLHOMINGPIGEON - Homing Pigeon</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLHOMINGPIGEON</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLIDENTICAL3CROWS - Identical Three Crows</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLIDENTICAL3CROWS</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLINNECK - In-Neck Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLINNECK</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLINVERTEDHAMMER - Inverted Hammer</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLINVERTEDHAMMER</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLKICKING - Kicking</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLKICKING</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLKICKINGBYLENGTH</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLLADDERBOTTOM - Ladder Bottom</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLLADDERBOTTOM</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLLONGLEGGEDDOJI - Long Legged Doji</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLLONGLEGGEDDOJI</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLLONGLINE - Long Line Candle</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLLONGLINE</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLMARUBOZU - Marubozu</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLMARUBOZU</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLMATCHINGLOW - Matching Low</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLMATCHINGLOW</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLMATHOLD - Mat Hold</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLMATHOLD</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">,</span> <span class="highlight n">penetration</span><span class="highlight o">=</span><span class="highlight mi">0</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLMORNINGDOJISTAR - Morning Doji Star</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLMORNINGDOJISTAR</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">,</span> <span class="highlight n">penetration</span><span class="highlight o">=</span><span class="highlight mi">0</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLMORNINGSTAR - Morning Star</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLMORNINGSTAR</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">,</span> <span class="highlight n">penetration</span><span class="highlight o">=</span><span class="highlight mi">0</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLONNECK - On-Neck Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLONNECK</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLPIERCING - Piercing Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLPIERCING</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLRICKSHAWMAN - Rickshaw Man</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLRICKSHAWMAN</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLRISEFALL3METHODS - Rising/Falling Three Methods</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLRISEFALL3METHODS</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLSEPARATINGLINES - Separating Lines</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLSEPARATINGLINES</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLSHOOTINGSTAR - Shooting Star</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLSHOOTINGSTAR</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLSHORTLINE - Short Line Candle</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLSHORTLINE</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLSPINNINGTOP - Spinning Top</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLSPINNINGTOP</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLSTALLEDPATTERN - Stalled Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLSTALLEDPATTERN</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLSTICKSANDWICH - Stick Sandwich</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLSTICKSANDWICH</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLTAKURI</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLTASUKIGAP - Tasuki Gap</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLTASUKIGAP</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLTHRUSTING - Thrusting Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLTHRUSTING</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLTRISTAR - Tristar Pattern</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLTRISTAR</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLUNIQUE3RIVER - Unique 3 River</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLUNIQUE3RIVER</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLUPSIDEGAP2CROWS - Upside Gap Two Crows</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLUPSIDEGAP2CROWS</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<h3>CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods</h3>
<div class="highlight"><pre><span></span><span class="highlight n">integer</span> <span class="highlight o">=</span> <span class="highlight n">CDLXSIDEGAP3METHODS</span><span class="highlight p">(</span><span class="highlight nb">open</span><span class="highlight p">,</span> <span class="highlight n">high</span><span class="highlight p">,</span> <span class="highlight n">low</span><span class="highlight p">,</span> <span class="highlight n">close</span><span class="highlight p">)</span>
</pre></div>
<p><a href="../doc_index.html">Documentation Index</a>
<a class="float-right" href="../funcs.html">All Function Groups</a></p>
        </section>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')
section = soup.find('section')
h3s = section.find_all('h3')
obj = {}
for h3 in h3s:
    txt = h3.text 
    value = txt.split('-',1)[0].strip()
    key = txt.split('-',1)[1].strip()
    obj.update({key:value})
import json
with open('static/pattern.json','w') as file:
    json.dump(obj,file)