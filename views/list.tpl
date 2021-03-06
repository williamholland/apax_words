<div class="content mt-4">

  <textarea id="wordListTextArea" class="textarea" placeholder="words">{{words}}</textarea>

  <div class="field is-grouped is-grouped-right">
    <p class="control">
      <button type="button" onclick="copyTextArea()" class="button is-link is-outlined -light mt-4 float-right">
        <span class="material-icons">content_copy</span><span class="ml-1">copy</span>
      </button>
    </p>
    <p class="control">
      <a class="button is-link is-outlined -light mt-4 float-right"
         href=".?quantity={{quantity}}&level={{level}}&seed=get"
      >
        <span class="material-icons">refresh</span><span class="ml-1">change</span>
      </a>
    </p>
  </div>

</div>
