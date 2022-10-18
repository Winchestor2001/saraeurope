function initSidebarClicker(clicker_tag,show_icon,close_icon,parent_tag)
{
  if(parent_tag===undefined || parent_tag===null){
    parent_tag='sidebar-product'
  }
  if(show_icon===undefined || show_icon===null){
    show_icon=''
  }
  if(close_icon===undefined || close_icon===null){
    close_icon=''
  }
  var parent_obj=$('.'+parent_tag)
  parent_obj.find('dd').hide();
  $.each(parent_obj.find('dl'), function (k, v) {
    if ($(v).find('dd').length > 0 && show_icon!=='') {
      var show_clicker='<'+clicker_tag+'>'+show_icon+'</'+clicker_tag+'>'
        $(v).prepend(show_clicker)
    }
  })
  parent_obj.find(clicker_tag).click(function () {
    var thisDd = $(this).parent().find('dd')

      if (thisDd.is(':visible')) {
        thisDd.slideUp(300)
        $(this).removeClass('clicker_active')
        if(show_icon!==''){
          $(this).html(show_icon)
        }
      } else {
        var otherDd = parent_obj.find('dd:visible')
        var otherDt = parent_obj.find(clicker_tag+'.clicker_active')
        otherDd.slideUp(300, function () {
          otherDt.removeClass('clicker_active')
          if(show_icon!==''){
            otherDt.html(show_icon)
          }
        })
        thisDd.slideDown(300)
        $(this).addClass('clicker_active')
        if(close_icon!==''){
          $(this).html(close_icon)
        }

      }

  })
}