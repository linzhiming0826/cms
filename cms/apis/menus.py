# -*- coding: utf-8 -*-
from menu.models import Menu


class Menus(object):
    def _get_menus_db(self):
        return Menu.objects.filter(show=1)

    def _get_first_menus(self, menus):
        first_menus = []
        for menu in menus:
            if not menu.parent_id or menu.parent_id <= 0:
                first_menus.append({
                    'parent_id': menu.parent_id,
                    'name': menu.name,
                    'url': menu.url,
                    'icon_class': menu.icon_class,
                    'id': menu.id,
                    'code': menu.code,
                    'second_menus': []
                })
        return first_menus

    def _get_second_menus(self, first_menus, menus):
        for first_menu in first_menus:
            for menu in menus:
                if menu.parent_id == first_menu['id']:
                    second_menus = {
                        'parent_id': menu.parent_id,
                        'name': menu.name,
                        'url': menu.url,
                        'icon_class': menu.icon_class,
                        'id': menu.id,
                        'code': menu.code
                    }
                    first_menu['second_menus'].append(second_menus)

    def _get_menus(self, menus):
        first_menus = self._get_first_menus(menus)
        self._get_second_menus(first_menus, menus)
        return first_menus

    def _handle_second_menus(self, second_menus, request):
        second_list = []
        for second_menu in second_menus:
            code = 'menu.%s_view' % second_menu['code']
            if request.user.has_perm(code):
                second_list.append(second_menu)
        return second_list

    def _handle_menus(self, menus, request):
        menu_list = []
        for menu in menus:
            code = 'menu.%s_view' % menu['code']
            if not request.user.has_perm(code):
                if menu['second_menus']:
                    second_menus = self._handle_second_menus(
                        menu['second_menus'], request)
                    if second_menus:
                        menu['second_menus'] = second_menus
                        menu_list.append(menu)
            else:
                menu_list.append(menu)
        return menu_list

    def get_menus(self, request):
        '''
        1.获取所有的菜单
        2.进行菜单的组合（一二级菜单）
        3.进行组合后的权限判断
        '''
        menus = self._get_menus_db()
        if menus:
            menus_list = self._get_menus(menus)
            menus_list = self._handle_menus(menus_list, request)
            return menus_list
        return None
