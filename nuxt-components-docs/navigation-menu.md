<!-- source: https://ui.nuxt.com/components/navigation-menu --> # NavigationMenu

[NavigationMenu](https://reka-ui.com/docs/components/navigation-
menu)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/NavigationMenu.vue)

A list of links that can be displayed horizontally or vertically.

## Usage

### Items

Use the `items` prop as an array of objects with the following properties:

  * `label?: string`
  * `icon?: string`
  * `avatar?: AvatarProps`
  * `badge?: string | number | BadgeProps`
  * `trailingIcon?: string`
  * `type?: 'label' | 'link'`
  * `value?: string`
  * `disabled?: boolean`
  * `class?: any`
  * `slot?: string`
  * `onSelect?(e: Event): void`
  * `children?: NavigationMenuChildItem[]`

You can pass any property from the [Link](/components/link#props) component
such as `to`, `target`, etc.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = ref<NavigationMenuItem[]>([
      {
        label: 'Guide',
        icon: 'i-lucide-book-open',
        to: '/getting-started',
        children: [
          {
            label: 'Introduction',
            description: 'Fully styled and customizable components for Nuxt.',
            icon: 'i-lucide-house'
          },
          {
            label: 'Installation',
            description: 'Learn how to install and configure Nuxt UI in your application.',
            icon: 'i-lucide-cloud-download'
          },
          {
            label: 'Icons',
            icon: 'i-lucide-smile',
            description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
          },
          {
            label: 'Colors',
            icon: 'i-lucide-swatch-book',
            description: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
          },
          {
            label: 'Theme',
            icon: 'i-lucide-cog',
            description: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
          }
        ]
      },
      {
        label: 'Composables',
        icon: 'i-lucide-database',
        to: '/composables',
        children: [
          {
            label: 'defineShortcuts',
            icon: 'i-lucide-file-text',
            description: 'Define shortcuts for your application.',
            to: '/composables/define-shortcuts'
          },
          {
            label: 'useOverlay',
            icon: 'i-lucide-file-text',
            description: 'Display a modal/slideover within your application.',
            to: '/composables/use-overlay'
          },
          {
            label: 'useToast',
            icon: 'i-lucide-file-text',
            description: 'Display a toast within your application.',
            to: '/composables/use-toast'
          }
        ]
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        to: '/components',
        active: true,
        children: [
          {
            label: 'Link',
            icon: 'i-lucide-file-text',
            description: 'Use NuxtLink with superpowers.',
            to: '/components/link'
          },
          {
            label: 'Modal',
            icon: 'i-lucide-file-text',
            description: 'Display a modal within your application.',
            to: '/components/modal'
          },
          {
            label: 'NavigationMenu',
            icon: 'i-lucide-file-text',
            description: 'Display a list of links.',
            to: '/components/navigation-menu'
          },
          {
            label: 'Pagination',
            icon: 'i-lucide-file-text',
            description: 'Display a list of pages.',
            to: '/components/pagination'
          },
          {
            label: 'Popover',
            icon: 'i-lucide-file-text',
            description: 'Display a non-modal dialog that floats around a trigger element.',
            to: '/components/popover'
          },
          {
            label: 'Progress',
            icon: 'i-lucide-file-text',
            description: 'Show a horizontal bar to indicate task progression.',
            to: '/components/progress'
          }
        ]
      },
      {
        label: 'GitHub',
        icon: 'i-simple-icons-github',
        badge: '3.8k',
        to: 'https://github.com/nuxt/ui',
        target: '_blank'
      },
      {
        label: 'Help',
        icon: 'i-lucide-circle-help',
        disabled: true
      }
    ])
    </script>
    
    <template>
      <UNavigationMenu :items="items" class="w-full justify-center" />
    </template>
    

Expand code

You can also pass an array of arrays to the `items` prop to display groups of
items.

Each item can take a `children` array of objects with the following properties
to create submenus:

  * `label: string`
  * `description?: string`
  * `icon?: string`
  * `class?: any`
  * `onSelect?(e: Event): void`

### Orientation

Use the `orientation` prop to change the orientation of the NavigationMenu.

When orientation is `vertical`, a [Collapsible](/components/collapsible)
component is used to display children. You can control the open state of each
item using the `open` and `defaultOpen` properties.

orientation

vertical

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = ref<NavigationMenuItem[][]>([
      [
        {
          label: 'Links',
          type: 'label'
        },
        {
          label: 'Guide',
          icon: 'i-lucide-book-open',
          children: [
            {
              label: 'Introduction',
              description: 'Fully styled and customizable components for Nuxt.',
              icon: 'i-lucide-house'
            },
            {
              label: 'Installation',
              description: 'Learn how to install and configure Nuxt UI in your application.',
              icon: 'i-lucide-cloud-download'
            },
            {
              label: 'Icons',
              icon: 'i-lucide-smile',
              description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
            },
            {
              label: 'Colors',
              icon: 'i-lucide-swatch-book',
              description: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
            },
            {
              label: 'Theme',
              icon: 'i-lucide-cog',
              description: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
            }
          ]
        },
        {
          label: 'Composables',
          icon: 'i-lucide-database',
          children: [
            {
              label: 'defineShortcuts',
              icon: 'i-lucide-file-text',
              description: 'Define shortcuts for your application.',
              to: '/composables/define-shortcuts'
            },
            {
              label: 'useOverlay',
              icon: 'i-lucide-file-text',
              description: 'Display a modal/slideover within your application.',
              to: '/composables/use-overlay'
            },
            {
              label: 'useToast',
              icon: 'i-lucide-file-text',
              description: 'Display a toast within your application.',
              to: '/composables/use-toast'
            }
          ]
        },
        {
          label: 'Components',
          icon: 'i-lucide-box',
          to: '/components',
          active: true,
          defaultOpen: true,
          children: [
            {
              label: 'Link',
              icon: 'i-lucide-file-text',
              description: 'Use NuxtLink with superpowers.',
              to: '/components/link'
            },
            {
              label: 'Modal',
              icon: 'i-lucide-file-text',
              description: 'Display a modal within your application.',
              to: '/components/modal'
            },
            {
              label: 'NavigationMenu',
              icon: 'i-lucide-file-text',
              description: 'Display a list of links.',
              to: '/components/navigation-menu'
            },
            {
              label: 'Pagination',
              icon: 'i-lucide-file-text',
              description: 'Display a list of pages.',
              to: '/components/pagination'
            },
            {
              label: 'Popover',
              icon: 'i-lucide-file-text',
              description: 'Display a non-modal dialog that floats around a trigger element.',
              to: '/components/popover'
            },
            {
              label: 'Progress',
              icon: 'i-lucide-file-text',
              description: 'Show a horizontal bar to indicate task progression.',
              to: '/components/progress'
            }
          ]
        }
      ],
      [
        {
          label: 'GitHub',
          icon: 'i-simple-icons-github',
          badge: '3.8k',
          to: 'https://github.com/nuxt/ui',
          target: '_blank'
        },
        {
          label: 'Help',
          icon: 'i-lucide-circle-help',
          disabled: true
        }
      ]
    ])
    </script>
    
    <template>
      <UNavigationMenu orientation="vertical" :items="items" class="data-[orientation=vertical]:w-48" />
    </template>
    

Expand code

Groups will be spaced when orientation is `horizontal` and separated when
orientation is `vertical`.

### Highlight

Use the `highlight` prop to display a highlighted border for the active item.

Use the `highlight-color` prop to change the color of the border. It defaults
to the `color` prop.

highlight

true

highlightColor

primary

orientation

horizontal

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = ref<NavigationMenuItem[][]>([
      [
        {
          label: 'Guide',
          icon: 'i-lucide-book-open',
          children: [
            {
              label: 'Introduction',
              description: 'Fully styled and customizable components for Nuxt.',
              icon: 'i-lucide-house'
            },
            {
              label: 'Installation',
              description: 'Learn how to install and configure Nuxt UI in your application.',
              icon: 'i-lucide-cloud-download'
            },
            {
              label: 'Icons',
              icon: 'i-lucide-smile',
              description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
            },
            {
              label: 'Colors',
              icon: 'i-lucide-swatch-book',
              description: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
            },
            {
              label: 'Theme',
              icon: 'i-lucide-cog',
              description:
                'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
            }
          ]
        },
        {
          label: 'Composables',
          icon: 'i-lucide-database',
          children: [
            {
              label: 'defineShortcuts',
              icon: 'i-lucide-file-text',
              description: 'Define shortcuts for your application.',
              to: '/composables/define-shortcuts'
            },
            {
              label: 'useOverlay',
              icon: 'i-lucide-file-text',
              description: 'Display a modal/slideover within your application.',
              to: '/composables/use-overlay'
            },
            {
              label: 'useToast',
              icon: 'i-lucide-file-text',
              description: 'Display a toast within your application.',
              to: '/composables/use-toast'
            }
          ]
        },
        {
          label: 'Components',
          icon: 'i-lucide-box',
          to: '/components',
          active: true,
          defaultOpen: true,
          children: [
            {
              label: 'Link',
              icon: 'i-lucide-file-text',
              description: 'Use NuxtLink with superpowers.',
              to: '/components/link'
            },
            {
              label: 'Modal',
              icon: 'i-lucide-file-text',
              description: 'Display a modal within your application.',
              to: '/components/modal'
            },
            {
              label: 'NavigationMenu',
              icon: 'i-lucide-file-text',
              description: 'Display a list of links.',
              to: '/components/navigation-menu'
            },
            {
              label: 'Pagination',
              icon: 'i-lucide-file-text',
              description: 'Display a list of pages.',
              to: '/components/pagination'
            },
            {
              label: 'Popover',
              icon: 'i-lucide-file-text',
              description: 'Display a non-modal dialog that floats around a trigger element.',
              to: '/components/popover'
            },
            {
              label: 'Progress',
              icon: 'i-lucide-file-text',
              description: 'Show a horizontal bar to indicate task progression.',
              to: '/components/progress'
            }
          ]
        }
      ],
      [
        {
          label: 'GitHub',
          icon: 'i-simple-icons-github',
          badge: '3.8k',
          to: 'https://github.com/nuxt/ui',
          target: '_blank'
        },
        {
          label: 'Help',
          icon: 'i-lucide-circle-help',
          disabled: true
        }
      ]
    ])
    </script>
    
    <template>
      <UNavigationMenu
        highlight
        highlight-color="primary"
        orientation="horizontal"
        :items="items"
        class="data-[orientation=horizontal]:border-b border-default data-[orientation=horizontal]:w-full data-[orientation=vertical]:w-48"
      />
    </template>
    

Expand code

In this example, the `border-b` class is applied to display a border in
`horizontal` orientation, this is not done by default to let you have a clean
slate to work with.

In `vertical` orientation, the `highlight` prop only highlights the border of
active children.

### Color

Use the `color` prop to change the color of the NavigationMenu.

color

neutral

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = ref<NavigationMenuItem[][]>([
      [
        {
          label: 'Guide',
          icon: 'i-lucide-book-open',
          to: '/getting-started'
        },
        {
          label: 'Composables',
          icon: 'i-lucide-database',
          to: '/composables'
        },
        {
          label: 'Components',
          icon: 'i-lucide-box',
          to: '/components',
          active: true
        }
      ],
      [
        {
          label: 'GitHub',
          icon: 'i-simple-icons-github',
          badge: '3.8k',
          to: 'https://github.com/nuxt/ui',
          target: '_blank'
        }
      ]
    ])
    </script>
    
    <template>
      <UNavigationMenu color="neutral" :items="items" class="w-full" />
    </template>
    

### Variant

Use the `variant` prop to change the variant of the NavigationMenu.

color

neutral

variant

link

highlight

false

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = ref<NavigationMenuItem[][]>([
      [
        {
          label: 'Guide',
          icon: 'i-lucide-book-open',
          to: '/getting-started'
        },
        {
          label: 'Composables',
          icon: 'i-lucide-database',
          to: '/composables'
        },
        {
          label: 'Components',
          icon: 'i-lucide-box',
          to: '/components',
          active: true
        }
      ],
      [
        {
          label: 'GitHub',
          icon: 'i-simple-icons-github',
          badge: '3.8k',
          to: 'https://github.com/nuxt/ui',
          target: '_blank'
        }
      ]
    ])
    </script>
    
    <template>
      <UNavigationMenu color="neutral" variant="link" :items="items" class="w-full" />
    </template>
    

The `highlight` prop changes the `pill` variant active item style. Try it out
to see the difference.

### Trailing Icon

Use the `trailing-icon` prop to customize the trailing
[Icon](/components/icon) of each item. Defaults to `i-lucide-chevron-down`.
This icon is only displayed when an item has children.

You can also set an icon for a specific item by using the `trailingIcon`
property in the item object.

trailingIcon

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = ref<NavigationMenuItem[]>([
      {
        label: 'Guide',
        icon: 'i-lucide-book-open',
        to: '/getting-started',
        children: [
          {
            label: 'Introduction',
            description: 'Fully styled and customizable components for Nuxt.',
            icon: 'i-lucide-house'
          },
          {
            label: 'Installation',
            description: 'Learn how to install and configure Nuxt UI in your application.',
            icon: 'i-lucide-cloud-download'
          },
          {
            label: 'Icons',
            icon: 'i-lucide-smile',
            description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
          },
          {
            label: 'Colors',
            icon: 'i-lucide-swatch-book',
            description: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
          },
          {
            label: 'Theme',
            icon: 'i-lucide-cog',
            description: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
          }
        ]
      },
      {
        label: 'Composables',
        icon: 'i-lucide-database',
        to: '/composables',
        children: [
          {
            label: 'defineShortcuts',
            icon: 'i-lucide-file-text',
            description: 'Define shortcuts for your application.',
            to: '/composables/define-shortcuts'
          },
          {
            label: 'useOverlay',
            icon: 'i-lucide-file-text',
            description: 'Display a modal/slideover within your application.',
            to: '/composables/use-overlay'
          },
          {
            label: 'useToast',
            icon: 'i-lucide-file-text',
            description: 'Display a toast within your application.',
            to: '/composables/use-toast'
          }
        ]
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        to: '/components',
        active: true,
        children: [
          {
            label: 'Link',
            icon: 'i-lucide-file-text',
            description: 'Use NuxtLink with superpowers.',
            to: '/components/link'
          },
          {
            label: 'Modal',
            icon: 'i-lucide-file-text',
            description: 'Display a modal within your application.',
            to: '/components/modal'
          },
          {
            label: 'NavigationMenu',
            icon: 'i-lucide-file-text',
            description: 'Display a list of links.',
            to: '/components/navigation-menu'
          },
          {
            label: 'Pagination',
            icon: 'i-lucide-file-text',
            description: 'Display a list of pages.',
            to: '/components/pagination'
          },
          {
            label: 'Popover',
            icon: 'i-lucide-file-text',
            description: 'Display a non-modal dialog that floats around a trigger element.',
            to: '/components/popover'
          },
          {
            label: 'Progress',
            icon: 'i-lucide-file-text',
            description: 'Show a horizontal bar to indicate task progression.',
            to: '/components/progress'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UNavigationMenu trailing-icon="i-lucide-arrow-down" :items="items" class="w-full justify-center" />
    </template>
    

Expand code

[](/getting-started/icons/nuxt#theme)You can customize this icon globally in
your `app.config.ts` under `ui.icons.chevronDown` key.

[](/getting-started/icons/vue#theme)You can customize this icon globally in
your `vite.config.ts` under `ui.icons.chevronDown` key.

### Arrow

Use the `arrow` prop to display an arrow on the NavigationMenu content when
items have children.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = ref<NavigationMenuItem[]>([
      {
        label: 'Guide',
        icon: 'i-lucide-book-open',
        to: '/getting-started',
        children: [
          {
            label: 'Introduction',
            description: 'Fully styled and customizable components for Nuxt.',
            icon: 'i-lucide-house'
          },
          {
            label: 'Installation',
            description: 'Learn how to install and configure Nuxt UI in your application.',
            icon: 'i-lucide-cloud-download'
          },
          {
            label: 'Icons',
            icon: 'i-lucide-smile',
            description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
          },
          {
            label: 'Colors',
            icon: 'i-lucide-swatch-book',
            description: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
          },
          {
            label: 'Theme',
            icon: 'i-lucide-cog',
            description: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
          }
        ]
      },
      {
        label: 'Composables',
        icon: 'i-lucide-database',
        to: '/composables',
        children: [
          {
            label: 'defineShortcuts',
            icon: 'i-lucide-file-text',
            description: 'Define shortcuts for your application.',
            to: '/composables/define-shortcuts'
          },
          {
            label: 'useOverlay',
            icon: 'i-lucide-file-text',
            description: 'Display a modal/slideover within your application.',
            to: '/composables/use-overlay'
          },
          {
            label: 'useToast',
            icon: 'i-lucide-file-text',
            description: 'Display a toast within your application.',
            to: '/composables/use-toast'
          }
        ]
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        to: '/components',
        active: true,
        children: [
          {
            label: 'Link',
            icon: 'i-lucide-file-text',
            description: 'Use NuxtLink with superpowers.',
            to: '/components/link'
          },
          {
            label: 'Modal',
            icon: 'i-lucide-file-text',
            description: 'Display a modal within your application.',
            to: '/components/modal'
          },
          {
            label: 'NavigationMenu',
            icon: 'i-lucide-file-text',
            description: 'Display a list of links.',
            to: '/components/navigation-menu'
          },
          {
            label: 'Pagination',
            icon: 'i-lucide-file-text',
            description: 'Display a list of pages.',
            to: '/components/pagination'
          },
          {
            label: 'Popover',
            icon: 'i-lucide-file-text',
            description: 'Display a non-modal dialog that floats around a trigger element.',
            to: '/components/popover'
          },
          {
            label: 'Progress',
            icon: 'i-lucide-file-text',
            description: 'Show a horizontal bar to indicate task progression.',
            to: '/components/progress'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UNavigationMenu arrow :items="items" class="w-full justify-center" />
    </template>
    

Expand code

The arrow is animated to follow the active item.

### Content Orientation

Use the `content-orientation` prop to change the orientation of the content.

This prop only works when `orientation` is `horizontal`.

contentOrientation

vertical

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = ref<NavigationMenuItem[]>([
      {
        label: 'Guide',
        icon: 'i-lucide-book-open',
        to: '/getting-started',
        children: [
          {
            label: 'Introduction',
            description: 'Fully styled and customizable components for Nuxt.',
            icon: 'i-lucide-house'
          },
          {
            label: 'Installation',
            description: 'Learn how to install and configure Nuxt UI in your application.',
            icon: 'i-lucide-cloud-download'
          },
          {
            label: 'Icons',
            icon: 'i-lucide-smile',
            description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
          }
        ]
      },
      {
        label: 'Composables',
        icon: 'i-lucide-database',
        to: '/composables',
        children: [
          {
            label: 'defineShortcuts',
            icon: 'i-lucide-file-text',
            description: 'Define shortcuts for your application.',
            to: '/composables/define-shortcuts'
          },
          {
            label: 'useOverlay',
            icon: 'i-lucide-file-text',
            description: 'Display a modal/slideover within your application.',
            to: '/composables/use-overlay'
          },
          {
            label: 'useToast',
            icon: 'i-lucide-file-text',
            description: 'Display a toast within your application.',
            to: '/composables/use-toast'
          }
        ]
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        to: '/components',
        active: true,
        children: [
          {
            label: 'Link',
            icon: 'i-lucide-file-text',
            description: 'Use NuxtLink with superpowers.',
            to: '/components/link'
          },
          {
            label: 'Modal',
            icon: 'i-lucide-file-text',
            description: 'Display a modal within your application.',
            to: '/components/modal'
          },
          {
            label: 'NavigationMenu',
            icon: 'i-lucide-file-text',
            description: 'Display a list of links.',
            to: '/components/navigation-menu'
          },
          {
            label: 'Pagination',
            icon: 'i-lucide-file-text',
            description: 'Display a list of pages.',
            to: '/components/pagination'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UNavigationMenu arrow content-orientation="vertical" :items="items" class="w-full justify-center" />
    </template>
    

Expand code

### Unmount

Use the `unmount-on-hide` prop to control the content unmounting behavior.
Defaults to `true`.

unmountOnHide

false

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = ref<NavigationMenuItem[]>([
      {
        label: 'Guide',
        icon: 'i-lucide-book-open',
        to: '/getting-started',
        children: [
          {
            label: 'Introduction',
            description: 'Fully styled and customizable components for Nuxt.',
            icon: 'i-lucide-house'
          },
          {
            label: 'Installation',
            description: 'Learn how to install and configure Nuxt UI in your application.',
            icon: 'i-lucide-cloud-download'
          },
          {
            label: 'Icons',
            icon: 'i-lucide-smile',
            description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
          },
          {
            label: 'Colors',
            icon: 'i-lucide-swatch-book',
            description: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
          },
          {
            label: 'Theme',
            icon: 'i-lucide-cog',
            description: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
          }
        ]
      },
      {
        label: 'Composables',
        icon: 'i-lucide-database',
        to: '/composables',
        children: [
          {
            label: 'defineShortcuts',
            icon: 'i-lucide-file-text',
            description: 'Define shortcuts for your application.',
            to: '/composables/define-shortcuts'
          },
          {
            label: 'useOverlay',
            icon: 'i-lucide-file-text',
            description: 'Display a modal/slideover within your application.',
            to: '/composables/use-overlay'
          },
          {
            label: 'useToast',
            icon: 'i-lucide-file-text',
            description: 'Display a toast within your application.',
            to: '/composables/use-toast'
          }
        ]
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        to: '/components',
        active: true,
        children: [
          {
            label: 'Link',
            icon: 'i-lucide-file-text',
            description: 'Use NuxtLink with superpowers.',
            to: '/components/link'
          },
          {
            label: 'Modal',
            icon: 'i-lucide-file-text',
            description: 'Display a modal within your application.',
            to: '/components/modal'
          },
          {
            label: 'NavigationMenu',
            icon: 'i-lucide-file-text',
            description: 'Display a list of links.',
            to: '/components/navigation-menu'
          },
          {
            label: 'Pagination',
            icon: 'i-lucide-file-text',
            description: 'Display a list of pages.',
            to: '/components/pagination'
          },
          {
            label: 'Popover',
            icon: 'i-lucide-file-text',
            description: 'Display a non-modal dialog that floats around a trigger element.',
            to: '/components/popover'
          },
          {
            label: 'Progress',
            icon: 'i-lucide-file-text',
            description: 'Show a horizontal bar to indicate task progression.',
            to: '/components/progress'
          }
        ]
      }
    ])
    </script>
    
    <template>
      <UNavigationMenu :unmount-on-hide="false" :items="items" class="w-full justify-center" />
    </template>
    

Expand code

You can inspect the DOM to see each item's content being rendered.

## Examples

### Control active item

You can control the active item by using the `default-value` prop or the
`v-model` directive with the index of the item.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items: NavigationMenuItem[] = [
      {
        label: 'Guide',
        icon: 'i-lucide-book-open',
        children: [
          {
            label: 'Introduction',
            description: 'Fully styled and customizable components for Nuxt.',
            icon: 'i-lucide-house'
          },
          {
            label: 'Installation',
            description: 'Learn how to install and configure Nuxt UI in your application.',
            icon: 'i-lucide-cloud-download'
          },
          {
            label: 'Icons',
            icon: 'i-lucide-smile',
            description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
          },
          {
            label: 'Colors',
            icon: 'i-lucide-swatch-book',
            description: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
          },
          {
            label: 'Theme',
            icon: 'i-lucide-cog',
            description: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
          }
        ]
      },
      {
        label: 'Composables',
        icon: 'i-lucide-database',
        children: [
          {
            label: 'defineShortcuts',
            icon: 'i-lucide-file-text',
            description: 'Define shortcuts for your application.'
          },
          {
            label: 'useOverlay',
            icon: 'i-lucide-file-text',
            description: 'Display a modal/slideover within your application.'
          },
          {
            label: 'useToast',
            icon: 'i-lucide-file-text',
            description: 'Display a toast within your application.'
          }
        ]
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        children: [
          {
            label: 'Link',
            icon: 'i-lucide-file-text',
            description: 'Use NuxtLink with superpowers.'
          },
          {
            label: 'Modal',
            icon: 'i-lucide-file-text',
            description: 'Display a modal within your application.'
          },
          {
            label: 'NavigationMenu',
            icon: 'i-lucide-file-text',
            description: 'Display a list of links.'
          },
          {
            label: 'Pagination',
            icon: 'i-lucide-file-text',
            description: 'Display a list of pages.'
          },
          {
            label: 'Popover',
            icon: 'i-lucide-file-text',
            description: 'Display a non-modal dialog that floats around a trigger element.'
          },
          {
            label: 'Progress',
            icon: 'i-lucide-file-text',
            description: 'Show a horizontal bar to indicate task progression.'
          }
        ]
      }
    ]
    
    const active = ref()
    
    defineShortcuts({
      1: () => {
        active.value = '0'
      },
      2: () => {
        active.value = '1'
      },
      3: () => {
        active.value = '2'
      }
    })
    </script>
    
    <template>
      <UNavigationMenu v-model="active" :items="items" class="w-full justify-center" />
    </template>
    

Expand code

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can switch the active item by pressing `1`, `2`, or `3`.

You can also pass the `value` of one of the items if provided.

### With custom slot

Use the `slot` property to customize a specific item.

You will have access to the following slots:

  * `#{{ item.slot }}`
  * `#{{ item.slot }}-leading`
  * `#{{ item.slot }}-label`
  * `#{{ item.slot }}-trailing`
  * `#{{ item.slot }}-content`

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = [
      {
        label: 'Guide',
        icon: 'i-lucide-book-open'
      },
      {
        label: 'Composables',
        icon: 'i-lucide-database'
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        slot: 'components' as const
      }
    ] satisfies NavigationMenuItem[]
    </script>
    
    <template>
      <UNavigationMenu :items="items" class="w-full justify-center">
        <template #components-trailing>
          <UBadge label="44" variant="subtle" size="sm" />
        </template>
      </UNavigationMenu>
    </template>
    

You can also use the `#item`, `#item-leading`, `#item-label`, `#item-trailing`
and `#item-content` slots to customize all items.

### With content slot

Use the `#item-content` slot or the `slot` property (`#{{ item.slot
}}-content`) to customize the content of a specific item.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const items = [
      {
        label: 'Docs',
        icon: 'i-lucide-book-open',
        slot: 'docs' as const,
        children: [
          {
            label: 'Icons',
            description: 'You have nothing to do, @nuxt/icon will handle it automatically.'
          },
          {
            label: 'Colors',
            description: 'Choose a primary and a neutral color from your Tailwind CSS theme.'
          },
          {
            label: 'Theme',
            description: 'You can customize components by using the `class` / `ui` props or in your app.config.ts.'
          }
        ]
      },
      {
        label: 'Components',
        icon: 'i-lucide-box',
        slot: 'components' as const,
        children: [
          {
            label: 'Link',
            description: 'Use NuxtLink with superpowers.'
          },
          {
            label: 'Modal',
            description: 'Display a modal within your application.'
          },
          {
            label: 'NavigationMenu',
            description: 'Display a list of links.'
          },
          {
            label: 'Pagination',
            description: 'Display a list of pages.'
          },
          {
            label: 'Popover',
            description: 'Display a non-modal dialog that floats around a trigger element.'
          },
          {
            label: 'Progress',
            description: 'Show a horizontal bar to indicate task progression.'
          }
        ]
      },
      {
        label: 'GitHub',
        icon: 'i-simple-icons-github'
      }
    ] satisfies NavigationMenuItem[]
    </script>
    
    <template>
      <UNavigationMenu
        :items="items"
        class="w-full justify-center"
        :ui="{
          viewport: 'sm:w-(--reka-navigation-menu-viewport-width)',
          childList: 'sm:w-96',
          childLinkDescription: 'text-balance line-clamp-2'
        }"
      >
        <template #docs-content="{ item }">
          <ul class="grid gap-2 p-4 lg:w-[500px] lg:grid-cols-[minmax(0,.75fr)_minmax(0,1fr)]">
            <li class="row-span-3">
              <Placeholder class="size-full min-h-48" />
            </li>
    
            <li v-for="child in item.children" :key="child.label">
              <ULink class="text-sm text-left rounded-md p-3 transition-colors hover:bg-elevated/50">
                <p class="font-medium text-highlighted">
                  {{ child.label }}
                </p>
                <p class="text-muted line-clamp-2">
                  {{ child.description }}
                </p>
              </ULink>
            </li>
          </ul>
        </template>
      </UNavigationMenu>
    </template>
    

In this example, we add the `sm:w-(--reka-navigation-menu-viewport-width)`
class on the `viewport` to have a dynamic width. This requires to set a width
on the content's first child.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`trailingIcon`| `appConfig.ui.icons.chevronDown`| ` string`The icon displayed
to open the menu.  
`externalIcon`| `true`| ` string | false | true`The icon displayed when the item is an external link. Set to `false` to hide the external icon.  
`items`| | ` NavigationMenuItem[] | NavigationMenuItem[][]`Show properties

  * `label?: string`
  * `icon?: string`
  * `avatar?: AvatarProps`
  * `badge?: string | number | BadgeProps`Display a badge on the item. `{ size: 'sm', color: 'neutral', variant: 'outline' }`
  * `trailingIcon?: string`
  * `type?: "label" | "link"`The type of the item. The `label` type only works on `vertical` orientation. Defaults to `'link'`.
  * `slot?: string`
  * `value?: string`
  * `children?: NavigationMenuChildItem[]`
  * `onSelect?: ((e: Event) => void)`
  * `class?: any`
  * `to?: string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`Route Location the link should navigate to when clicked on.
  * `as?: any`The element or component this component should render as when not a link. Defaults to `'button'`.
  * `disabled?: boolean`
  * `active?: boolean`Force the link to be active independent of the current route.
  * `target?: "_blank" | "_parent" | "_self" | "_top" | (string & {}) | null`Where to display the linked URL, as the name for a browsing context.
  * `defaultOpen?: boolean`The open state of the collapsible when it is initially rendered.   
Use when you do not need to control its open state.

  * `open?: boolean`The controlled open state of the collapsible. Can be binded with `v-model`.

  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'pill'`| ` "pill" | "link"`  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`The orientation of the menu.  
`collapsed`| `false`| `boolean`Collapse the navigation menu to only show
icons. Only works when `orientation` is `vertical`.  
`highlight`| | `boolean`Display a line next to the active item.  
`highlightColor`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`content`| | ` NavigationMenuContentProps & Partial<EmitsToProps<DismissableLayerEmits>>`The content of the menu.Show properties

  * `disableOutsidePointerEvents?: boolean`When `true`, hover/focus/click interactions will be disabled on elements outside the `DismissableLayer`. Users will need to click twice on outside elements to interact with them: once to close the `DismissableLayer`, and again to trigger the element.
  * `onEscapeKeyDown?: ((event: KeyboardEvent) => void)`
  * `onPointerDownOutside?: ((event: PointerDownOutsideEvent) => void)`
  * `onFocusOutside?: ((event: FocusOutsideEvent) => void)`
  * `onInteractOutside?: ((event: PointerDownOutsideEvent | FocusOutsideEvent) => void)`

  
`contentOrientation`| `'horizontal'`| ` "horizontal" | "vertical"`The orientation of the content. Only works when `orientation` is `horizontal`.  
`arrow`| `false`| `boolean`Display an arrow alongside the menu.  
`labelKey`| `'label'`| ` string | number`The key used to get the label from the item.  
`modelValue`| | ` string`The controlled value of the menu item to activate. Can be used as `v-model`.  
`defaultValue`| | ` string`The value of the menu item that should be active when initially rendered.Use when you do not need to control the value state.  
`delayDuration`| `0`| ` number`The duration from when the pointer enters the
trigger until the tooltip gets opened.  
`disableClickTrigger`| `false`| `boolean`If `true`, menu cannot be open by
click on trigger  
`disableHoverTrigger`| `false`| `boolean`If `true`, menu cannot be open by
hover on trigger  
`skipDelayDuration`| `300`| ` number`How much time a user has to enter another
trigger without incurring a delay again.  
`disablePointerLeaveClose`| `false`| `boolean`If `true`, menu will not close
during pointer leave event  
`unmountOnHide`| `true`| `boolean`When `true`, the element will be unmounted
on closed state.  
`ui`| | ` { root?: ClassNameValue; list?: ClassNameValue; label?: ClassNameValue; item?: ClassNameValue; link?: ClassNameValue; ... 22 more ...; arrow?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`item`| `{ item: NavigationMenuItem; index: number; active?: boolean | undefined; }`  
`item-leading`| `{ item: NavigationMenuItem; index: number; active?: boolean | undefined; }`  
`item-label`| `{ item: NavigationMenuItem; index: number; active?: boolean | undefined; }`  
`item-trailing`| `{ item: NavigationMenuItem; index: number; active?: boolean | undefined; }`  
`item-content`| `{ item: NavigationMenuItem; index: number; active?: boolean | undefined; }`  
`list-leading`| `{}`  
`list-trailing`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:modelValue`| `[value: string]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        navigationMenu: {
          slots: {
            root: 'relative flex gap-1.5 [&>div]:min-w-0',
            list: 'isolate min-w-0',
            label: 'w-full flex items-center gap-1.5 font-semibold text-xs/5 text-highlighted px-2.5 py-1.5',
            item: 'min-w-0',
            link: 'group relative w-full flex items-center gap-1.5 font-medium text-sm before:absolute before:z-[-1] before:rounded-md focus:outline-none focus-visible:outline-none dark:focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2',
            linkLeadingIcon: 'shrink-0 size-5',
            linkLeadingAvatar: 'shrink-0',
            linkLeadingAvatarSize: '2xs',
            linkTrailing: 'ms-auto inline-flex gap-1.5 items-center',
            linkTrailingBadge: 'shrink-0',
            linkTrailingBadgeSize: 'sm',
            linkTrailingIcon: 'size-5 transform shrink-0 group-data-[state=open]:rotate-180 transition-transform duration-200',
            linkLabel: 'truncate',
            linkLabelExternalIcon: 'inline-block size-3 align-top text-dimmed',
            childList: '',
            childItem: '',
            childLink: 'group size-full px-3 py-2 rounded-md flex items-start gap-2 text-start',
            childLinkWrapper: 'flex flex-col items-start',
            childLinkIcon: 'size-5 shrink-0',
            childLinkLabel: 'font-semibold text-sm relative inline-flex',
            childLinkLabelExternalIcon: 'inline-block size-3 align-top text-dimmed',
            childLinkDescription: 'text-sm text-muted',
            separator: 'px-2 h-px bg-border',
            viewportWrapper: 'absolute top-full left-0 flex w-full',
            viewport: 'relative overflow-hidden bg-default shadow-lg rounded-md ring ring-default h-(--reka-navigation-menu-viewport-height) w-full transition-[width,height,left] duration-200 origin-[top_center] data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] z-[1]',
            content: 'absolute top-0 left-0 w-full sm:w-auto',
            indicator: 'absolute data-[state=visible]:animate-[fade-in_100ms_ease-out] data-[state=hidden]:animate-[fade-out_100ms_ease-in] data-[state=hidden]:opacity-0 bottom-0 z-[2] w-(--reka-navigation-menu-indicator-size) translate-x-(--reka-navigation-menu-indicator-position) flex h-2.5 items-end justify-center overflow-hidden transition-[translate,width] duration-200',
            arrow: 'relative top-[50%] size-2.5 rotate-45 border border-default bg-default z-[1] rounded-xs'
          },
          variants: {
            color: {
              primary: {
                link: 'focus-visible:before:ring-primary',
                childLink: 'focus-visible:outline-primary'
              },
              secondary: {
                link: 'focus-visible:before:ring-secondary',
                childLink: 'focus-visible:outline-secondary'
              },
              success: {
                link: 'focus-visible:before:ring-success',
                childLink: 'focus-visible:outline-success'
              },
              info: {
                link: 'focus-visible:before:ring-info',
                childLink: 'focus-visible:outline-info'
              },
              warning: {
                link: 'focus-visible:before:ring-warning',
                childLink: 'focus-visible:outline-warning'
              },
              error: {
                link: 'focus-visible:before:ring-error',
                childLink: 'focus-visible:outline-error'
              },
              neutral: {
                link: 'focus-visible:before:ring-inverted',
                childLink: 'focus-visible:outline-inverted'
              }
            },
            highlightColor: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            variant: {
              pill: '',
              link: ''
            },
            orientation: {
              horizontal: {
                root: 'items-center justify-between',
                list: 'flex items-center',
                item: 'py-2',
                link: 'px-2.5 py-1.5 before:inset-x-px before:inset-y-0',
                childList: 'grid p-2'
              },
              vertical: {
                root: 'flex-col',
                link: 'flex-row px-2.5 py-1.5 before:inset-y-px before:inset-x-0'
              }
            },
            contentOrientation: {
              horizontal: {
                viewportWrapper: 'justify-center',
                content: 'data-[motion=from-start]:animate-[enter-from-left_200ms_ease] data-[motion=from-end]:animate-[enter-from-right_200ms_ease] data-[motion=to-start]:animate-[exit-to-left_200ms_ease] data-[motion=to-end]:animate-[exit-to-right_200ms_ease]'
              },
              vertical: {
                viewport: 'sm:w-(--reka-navigation-menu-viewport-width) left-(--reka-navigation-menu-viewport-left)'
              }
            },
            active: {
              true: {
                childLink: 'bg-elevated text-highlighted',
                childLinkIcon: 'text-default'
              },
              false: {
                link: 'text-muted',
                linkLeadingIcon: 'text-dimmed',
                childLink: [
                  'hover:bg-elevated/50 text-default hover:text-highlighted',
                  'transition-colors'
                ],
                childLinkIcon: [
                  'text-dimmed group-hover:text-default',
                  'transition-colors'
                ]
              }
            },
            disabled: {
              true: {
                link: 'cursor-not-allowed opacity-75'
              }
            },
            highlight: {
              true: ''
            },
            level: {
              true: ''
            },
            collapsed: {
              true: ''
            }
          },
          compoundVariants: [
            {
              orientation: 'horizontal',
              contentOrientation: 'horizontal',
              class: {
                childList: 'grid-cols-2 gap-2'
              }
            },
            {
              orientation: 'horizontal',
              contentOrientation: 'vertical',
              class: {
                childList: 'gap-1',
                content: 'w-60'
              }
            },
            {
              orientation: 'horizontal',
              highlight: true,
              class: {
                link: [
                  'after:absolute after:-bottom-2 after:inset-x-2.5 after:block after:h-px after:rounded-full',
                  'after:transition-colors'
                ]
              }
            },
            {
              orientation: 'vertical',
              highlight: true,
              level: true,
              class: {
                link: [
                  'after:absolute after:-start-1.5 after:inset-y-0.5 after:block after:w-px after:rounded-full',
                  'after:transition-colors'
                ]
              }
            },
            {
              disabled: false,
              active: false,
              variant: 'pill',
              class: {
                link: [
                  'hover:text-highlighted hover:before:bg-elevated/50',
                  'transition-colors before:transition-colors'
                ],
                linkLeadingIcon: [
                  'group-hover:text-default',
                  'transition-colors'
                ]
              }
            },
            {
              disabled: false,
              active: false,
              variant: 'pill',
              orientation: 'horizontal',
              class: {
                link: 'data-[state=open]:text-highlighted',
                linkLeadingIcon: 'group-data-[state=open]:text-default'
              }
            },
            {
              disabled: false,
              variant: 'pill',
              highlight: true,
              orientation: 'horizontal',
              class: {
                link: 'data-[state=open]:before:bg-elevated/50'
              }
            },
            {
              disabled: false,
              variant: 'pill',
              highlight: false,
              active: false,
              orientation: 'horizontal',
              class: {
                link: 'data-[state=open]:before:bg-elevated/50'
              }
            },
            {
              color: 'primary',
              variant: 'pill',
              active: true,
              class: {
                link: 'text-primary',
                linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
              }
            },
            {
              color: 'neutral',
              variant: 'pill',
              active: true,
              class: {
                link: 'text-highlighted',
                linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
              }
            },
            {
              variant: 'pill',
              active: true,
              highlight: false,
              class: {
                link: 'before:bg-elevated'
              }
            },
            {
              variant: 'pill',
              active: true,
              highlight: true,
              class: {
                link: [
                  'hover:before:bg-elevated/50',
                  'before:transition-colors'
                ]
              }
            },
            {
              disabled: false,
              active: false,
              variant: 'link',
              class: {
                link: [
                  'hover:text-highlighted',
                  'transition-colors'
                ],
                linkLeadingIcon: [
                  'group-hover:text-default',
                  'transition-colors'
                ]
              }
            },
            {
              disabled: false,
              active: false,
              variant: 'link',
              orientation: 'horizontal',
              class: {
                link: 'data-[state=open]:text-highlighted',
                linkLeadingIcon: 'group-data-[state=open]:text-default'
              }
            },
            {
              color: 'primary',
              variant: 'link',
              active: true,
              class: {
                link: 'text-primary',
                linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
              }
            },
            {
              color: 'neutral',
              variant: 'link',
              active: true,
              class: {
                link: 'text-highlighted',
                linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
              }
            },
            {
              highlightColor: 'primary',
              highlight: true,
              level: true,
              active: true,
              class: {
                link: 'after:bg-primary'
              }
            },
            {
              highlightColor: 'neutral',
              highlight: true,
              level: true,
              active: true,
              class: {
                link: 'after:bg-inverted'
              }
            },
            {
              orientation: 'vertical',
              collapsed: false,
              class: {
                childList: 'ms-5 border-s border-default',
                childItem: 'ps-1.5 -ms-px'
              }
            },
            {
              orientation: 'vertical',
              collapsed: true,
              class: {
                link: 'px-1.5'
              }
            }
          ],
          defaultVariants: {
            color: 'primary',
            highlightColor: 'primary',
            variant: 'pill'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            navigationMenu: {
              slots: {
                root: 'relative flex gap-1.5 [&>div]:min-w-0',
                list: 'isolate min-w-0',
                label: 'w-full flex items-center gap-1.5 font-semibold text-xs/5 text-highlighted px-2.5 py-1.5',
                item: 'min-w-0',
                link: 'group relative w-full flex items-center gap-1.5 font-medium text-sm before:absolute before:z-[-1] before:rounded-md focus:outline-none focus-visible:outline-none dark:focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2',
                linkLeadingIcon: 'shrink-0 size-5',
                linkLeadingAvatar: 'shrink-0',
                linkLeadingAvatarSize: '2xs',
                linkTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                linkTrailingBadge: 'shrink-0',
                linkTrailingBadgeSize: 'sm',
                linkTrailingIcon: 'size-5 transform shrink-0 group-data-[state=open]:rotate-180 transition-transform duration-200',
                linkLabel: 'truncate',
                linkLabelExternalIcon: 'inline-block size-3 align-top text-dimmed',
                childList: '',
                childItem: '',
                childLink: 'group size-full px-3 py-2 rounded-md flex items-start gap-2 text-start',
                childLinkWrapper: 'flex flex-col items-start',
                childLinkIcon: 'size-5 shrink-0',
                childLinkLabel: 'font-semibold text-sm relative inline-flex',
                childLinkLabelExternalIcon: 'inline-block size-3 align-top text-dimmed',
                childLinkDescription: 'text-sm text-muted',
                separator: 'px-2 h-px bg-border',
                viewportWrapper: 'absolute top-full left-0 flex w-full',
                viewport: 'relative overflow-hidden bg-default shadow-lg rounded-md ring ring-default h-(--reka-navigation-menu-viewport-height) w-full transition-[width,height,left] duration-200 origin-[top_center] data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] z-[1]',
                content: 'absolute top-0 left-0 w-full sm:w-auto',
                indicator: 'absolute data-[state=visible]:animate-[fade-in_100ms_ease-out] data-[state=hidden]:animate-[fade-out_100ms_ease-in] data-[state=hidden]:opacity-0 bottom-0 z-[2] w-(--reka-navigation-menu-indicator-size) translate-x-(--reka-navigation-menu-indicator-position) flex h-2.5 items-end justify-center overflow-hidden transition-[translate,width] duration-200',
                arrow: 'relative top-[50%] size-2.5 rotate-45 border border-default bg-default z-[1] rounded-xs'
              },
              variants: {
                color: {
                  primary: {
                    link: 'focus-visible:before:ring-primary',
                    childLink: 'focus-visible:outline-primary'
                  },
                  secondary: {
                    link: 'focus-visible:before:ring-secondary',
                    childLink: 'focus-visible:outline-secondary'
                  },
                  success: {
                    link: 'focus-visible:before:ring-success',
                    childLink: 'focus-visible:outline-success'
                  },
                  info: {
                    link: 'focus-visible:before:ring-info',
                    childLink: 'focus-visible:outline-info'
                  },
                  warning: {
                    link: 'focus-visible:before:ring-warning',
                    childLink: 'focus-visible:outline-warning'
                  },
                  error: {
                    link: 'focus-visible:before:ring-error',
                    childLink: 'focus-visible:outline-error'
                  },
                  neutral: {
                    link: 'focus-visible:before:ring-inverted',
                    childLink: 'focus-visible:outline-inverted'
                  }
                },
                highlightColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                variant: {
                  pill: '',
                  link: ''
                },
                orientation: {
                  horizontal: {
                    root: 'items-center justify-between',
                    list: 'flex items-center',
                    item: 'py-2',
                    link: 'px-2.5 py-1.5 before:inset-x-px before:inset-y-0',
                    childList: 'grid p-2'
                  },
                  vertical: {
                    root: 'flex-col',
                    link: 'flex-row px-2.5 py-1.5 before:inset-y-px before:inset-x-0'
                  }
                },
                contentOrientation: {
                  horizontal: {
                    viewportWrapper: 'justify-center',
                    content: 'data-[motion=from-start]:animate-[enter-from-left_200ms_ease] data-[motion=from-end]:animate-[enter-from-right_200ms_ease] data-[motion=to-start]:animate-[exit-to-left_200ms_ease] data-[motion=to-end]:animate-[exit-to-right_200ms_ease]'
                  },
                  vertical: {
                    viewport: 'sm:w-(--reka-navigation-menu-viewport-width) left-(--reka-navigation-menu-viewport-left)'
                  }
                },
                active: {
                  true: {
                    childLink: 'bg-elevated text-highlighted',
                    childLinkIcon: 'text-default'
                  },
                  false: {
                    link: 'text-muted',
                    linkLeadingIcon: 'text-dimmed',
                    childLink: [
                      'hover:bg-elevated/50 text-default hover:text-highlighted',
                      'transition-colors'
                    ],
                    childLinkIcon: [
                      'text-dimmed group-hover:text-default',
                      'transition-colors'
                    ]
                  }
                },
                disabled: {
                  true: {
                    link: 'cursor-not-allowed opacity-75'
                  }
                },
                highlight: {
                  true: ''
                },
                level: {
                  true: ''
                },
                collapsed: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  contentOrientation: 'horizontal',
                  class: {
                    childList: 'grid-cols-2 gap-2'
                  }
                },
                {
                  orientation: 'horizontal',
                  contentOrientation: 'vertical',
                  class: {
                    childList: 'gap-1',
                    content: 'w-60'
                  }
                },
                {
                  orientation: 'horizontal',
                  highlight: true,
                  class: {
                    link: [
                      'after:absolute after:-bottom-2 after:inset-x-2.5 after:block after:h-px after:rounded-full',
                      'after:transition-colors'
                    ]
                  }
                },
                {
                  orientation: 'vertical',
                  highlight: true,
                  level: true,
                  class: {
                    link: [
                      'after:absolute after:-start-1.5 after:inset-y-0.5 after:block after:w-px after:rounded-full',
                      'after:transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'pill',
                  class: {
                    link: [
                      'hover:text-highlighted hover:before:bg-elevated/50',
                      'transition-colors before:transition-colors'
                    ],
                    linkLeadingIcon: [
                      'group-hover:text-default',
                      'transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'pill',
                  orientation: 'horizontal',
                  class: {
                    link: 'data-[state=open]:text-highlighted',
                    linkLeadingIcon: 'group-data-[state=open]:text-default'
                  }
                },
                {
                  disabled: false,
                  variant: 'pill',
                  highlight: true,
                  orientation: 'horizontal',
                  class: {
                    link: 'data-[state=open]:before:bg-elevated/50'
                  }
                },
                {
                  disabled: false,
                  variant: 'pill',
                  highlight: false,
                  active: false,
                  orientation: 'horizontal',
                  class: {
                    link: 'data-[state=open]:before:bg-elevated/50'
                  }
                },
                {
                  color: 'primary',
                  variant: 'pill',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'pill',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
                  }
                },
                {
                  variant: 'pill',
                  active: true,
                  highlight: false,
                  class: {
                    link: 'before:bg-elevated'
                  }
                },
                {
                  variant: 'pill',
                  active: true,
                  highlight: true,
                  class: {
                    link: [
                      'hover:before:bg-elevated/50',
                      'before:transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'link',
                  class: {
                    link: [
                      'hover:text-highlighted',
                      'transition-colors'
                    ],
                    linkLeadingIcon: [
                      'group-hover:text-default',
                      'transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'link',
                  orientation: 'horizontal',
                  class: {
                    link: 'data-[state=open]:text-highlighted',
                    linkLeadingIcon: 'group-data-[state=open]:text-default'
                  }
                },
                {
                  color: 'primary',
                  variant: 'link',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'link',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
                  }
                },
                {
                  highlightColor: 'primary',
                  highlight: true,
                  level: true,
                  active: true,
                  class: {
                    link: 'after:bg-primary'
                  }
                },
                {
                  highlightColor: 'neutral',
                  highlight: true,
                  level: true,
                  active: true,
                  class: {
                    link: 'after:bg-inverted'
                  }
                },
                {
                  orientation: 'vertical',
                  collapsed: false,
                  class: {
                    childList: 'ms-5 border-s border-default',
                    childItem: 'ps-1.5 -ms-px'
                  }
                },
                {
                  orientation: 'vertical',
                  collapsed: true,
                  class: {
                    link: 'px-1.5'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                highlightColor: 'primary',
                variant: 'pill'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            navigationMenu: {
              slots: {
                root: 'relative flex gap-1.5 [&>div]:min-w-0',
                list: 'isolate min-w-0',
                label: 'w-full flex items-center gap-1.5 font-semibold text-xs/5 text-highlighted px-2.5 py-1.5',
                item: 'min-w-0',
                link: 'group relative w-full flex items-center gap-1.5 font-medium text-sm before:absolute before:z-[-1] before:rounded-md focus:outline-none focus-visible:outline-none dark:focus-visible:outline-none focus-visible:before:ring-inset focus-visible:before:ring-2',
                linkLeadingIcon: 'shrink-0 size-5',
                linkLeadingAvatar: 'shrink-0',
                linkLeadingAvatarSize: '2xs',
                linkTrailing: 'ms-auto inline-flex gap-1.5 items-center',
                linkTrailingBadge: 'shrink-0',
                linkTrailingBadgeSize: 'sm',
                linkTrailingIcon: 'size-5 transform shrink-0 group-data-[state=open]:rotate-180 transition-transform duration-200',
                linkLabel: 'truncate',
                linkLabelExternalIcon: 'inline-block size-3 align-top text-dimmed',
                childList: '',
                childItem: '',
                childLink: 'group size-full px-3 py-2 rounded-md flex items-start gap-2 text-start',
                childLinkWrapper: 'flex flex-col items-start',
                childLinkIcon: 'size-5 shrink-0',
                childLinkLabel: 'font-semibold text-sm relative inline-flex',
                childLinkLabelExternalIcon: 'inline-block size-3 align-top text-dimmed',
                childLinkDescription: 'text-sm text-muted',
                separator: 'px-2 h-px bg-border',
                viewportWrapper: 'absolute top-full left-0 flex w-full',
                viewport: 'relative overflow-hidden bg-default shadow-lg rounded-md ring ring-default h-(--reka-navigation-menu-viewport-height) w-full transition-[width,height,left] duration-200 origin-[top_center] data-[state=open]:animate-[scale-in_100ms_ease-out] data-[state=closed]:animate-[scale-out_100ms_ease-in] z-[1]',
                content: 'absolute top-0 left-0 w-full sm:w-auto',
                indicator: 'absolute data-[state=visible]:animate-[fade-in_100ms_ease-out] data-[state=hidden]:animate-[fade-out_100ms_ease-in] data-[state=hidden]:opacity-0 bottom-0 z-[2] w-(--reka-navigation-menu-indicator-size) translate-x-(--reka-navigation-menu-indicator-position) flex h-2.5 items-end justify-center overflow-hidden transition-[translate,width] duration-200',
                arrow: 'relative top-[50%] size-2.5 rotate-45 border border-default bg-default z-[1] rounded-xs'
              },
              variants: {
                color: {
                  primary: {
                    link: 'focus-visible:before:ring-primary',
                    childLink: 'focus-visible:outline-primary'
                  },
                  secondary: {
                    link: 'focus-visible:before:ring-secondary',
                    childLink: 'focus-visible:outline-secondary'
                  },
                  success: {
                    link: 'focus-visible:before:ring-success',
                    childLink: 'focus-visible:outline-success'
                  },
                  info: {
                    link: 'focus-visible:before:ring-info',
                    childLink: 'focus-visible:outline-info'
                  },
                  warning: {
                    link: 'focus-visible:before:ring-warning',
                    childLink: 'focus-visible:outline-warning'
                  },
                  error: {
                    link: 'focus-visible:before:ring-error',
                    childLink: 'focus-visible:outline-error'
                  },
                  neutral: {
                    link: 'focus-visible:before:ring-inverted',
                    childLink: 'focus-visible:outline-inverted'
                  }
                },
                highlightColor: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                variant: {
                  pill: '',
                  link: ''
                },
                orientation: {
                  horizontal: {
                    root: 'items-center justify-between',
                    list: 'flex items-center',
                    item: 'py-2',
                    link: 'px-2.5 py-1.5 before:inset-x-px before:inset-y-0',
                    childList: 'grid p-2'
                  },
                  vertical: {
                    root: 'flex-col',
                    link: 'flex-row px-2.5 py-1.5 before:inset-y-px before:inset-x-0'
                  }
                },
                contentOrientation: {
                  horizontal: {
                    viewportWrapper: 'justify-center',
                    content: 'data-[motion=from-start]:animate-[enter-from-left_200ms_ease] data-[motion=from-end]:animate-[enter-from-right_200ms_ease] data-[motion=to-start]:animate-[exit-to-left_200ms_ease] data-[motion=to-end]:animate-[exit-to-right_200ms_ease]'
                  },
                  vertical: {
                    viewport: 'sm:w-(--reka-navigation-menu-viewport-width) left-(--reka-navigation-menu-viewport-left)'
                  }
                },
                active: {
                  true: {
                    childLink: 'bg-elevated text-highlighted',
                    childLinkIcon: 'text-default'
                  },
                  false: {
                    link: 'text-muted',
                    linkLeadingIcon: 'text-dimmed',
                    childLink: [
                      'hover:bg-elevated/50 text-default hover:text-highlighted',
                      'transition-colors'
                    ],
                    childLinkIcon: [
                      'text-dimmed group-hover:text-default',
                      'transition-colors'
                    ]
                  }
                },
                disabled: {
                  true: {
                    link: 'cursor-not-allowed opacity-75'
                  }
                },
                highlight: {
                  true: ''
                },
                level: {
                  true: ''
                },
                collapsed: {
                  true: ''
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  contentOrientation: 'horizontal',
                  class: {
                    childList: 'grid-cols-2 gap-2'
                  }
                },
                {
                  orientation: 'horizontal',
                  contentOrientation: 'vertical',
                  class: {
                    childList: 'gap-1',
                    content: 'w-60'
                  }
                },
                {
                  orientation: 'horizontal',
                  highlight: true,
                  class: {
                    link: [
                      'after:absolute after:-bottom-2 after:inset-x-2.5 after:block after:h-px after:rounded-full',
                      'after:transition-colors'
                    ]
                  }
                },
                {
                  orientation: 'vertical',
                  highlight: true,
                  level: true,
                  class: {
                    link: [
                      'after:absolute after:-start-1.5 after:inset-y-0.5 after:block after:w-px after:rounded-full',
                      'after:transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'pill',
                  class: {
                    link: [
                      'hover:text-highlighted hover:before:bg-elevated/50',
                      'transition-colors before:transition-colors'
                    ],
                    linkLeadingIcon: [
                      'group-hover:text-default',
                      'transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'pill',
                  orientation: 'horizontal',
                  class: {
                    link: 'data-[state=open]:text-highlighted',
                    linkLeadingIcon: 'group-data-[state=open]:text-default'
                  }
                },
                {
                  disabled: false,
                  variant: 'pill',
                  highlight: true,
                  orientation: 'horizontal',
                  class: {
                    link: 'data-[state=open]:before:bg-elevated/50'
                  }
                },
                {
                  disabled: false,
                  variant: 'pill',
                  highlight: false,
                  active: false,
                  orientation: 'horizontal',
                  class: {
                    link: 'data-[state=open]:before:bg-elevated/50'
                  }
                },
                {
                  color: 'primary',
                  variant: 'pill',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'pill',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
                  }
                },
                {
                  variant: 'pill',
                  active: true,
                  highlight: false,
                  class: {
                    link: 'before:bg-elevated'
                  }
                },
                {
                  variant: 'pill',
                  active: true,
                  highlight: true,
                  class: {
                    link: [
                      'hover:before:bg-elevated/50',
                      'before:transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'link',
                  class: {
                    link: [
                      'hover:text-highlighted',
                      'transition-colors'
                    ],
                    linkLeadingIcon: [
                      'group-hover:text-default',
                      'transition-colors'
                    ]
                  }
                },
                {
                  disabled: false,
                  active: false,
                  variant: 'link',
                  orientation: 'horizontal',
                  class: {
                    link: 'data-[state=open]:text-highlighted',
                    linkLeadingIcon: 'group-data-[state=open]:text-default'
                  }
                },
                {
                  color: 'primary',
                  variant: 'link',
                  active: true,
                  class: {
                    link: 'text-primary',
                    linkLeadingIcon: 'text-primary group-data-[state=open]:text-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'link',
                  active: true,
                  class: {
                    link: 'text-highlighted',
                    linkLeadingIcon: 'text-highlighted group-data-[state=open]:text-highlighted'
                  }
                },
                {
                  highlightColor: 'primary',
                  highlight: true,
                  level: true,
                  active: true,
                  class: {
                    link: 'after:bg-primary'
                  }
                },
                {
                  highlightColor: 'neutral',
                  highlight: true,
                  level: true,
                  active: true,
                  class: {
                    link: 'after:bg-inverted'
                  }
                },
                {
                  orientation: 'vertical',
                  collapsed: false,
                  class: {
                    childList: 'ms-5 border-s border-default',
                    childItem: 'ps-1.5 -ms-px'
                  }
                },
                {
                  orientation: 'vertical',
                  collapsed: true,
                  class: {
                    link: 'px-1.5'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                highlightColor: 'primary',
                variant: 'pill'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/navigation-menu.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[ModalA dialog window that can be used to display a message or request user
input.](/components/modal)[PaginationA list of buttons or links to navigate
through pages.](/components/pagination)

