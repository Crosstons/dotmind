import { Icon } from '@iconify/react';

import { SideNavItem } from './types';

export const SIDENAV_ITEMS: SideNavItem[] = [
  {
    title: 'Chats',
    path: '/',
    icon: <Icon icon="lucide:message-square" width="24" height="24" />,
  },
  {
    title: 'Data',
    path: '/settings',
    icon: <Icon icon="lucide:settings" width="24" height="24" />,
    submenu: true,
    subMenuItems: [
      { title: 'Address Book', path: '/settings/account' },
      { title: 'Transfers', path: '/settings/transfers' },
      { title: 'Key Pairs', path: '/settings/keypair' }
    ],
  },
];
