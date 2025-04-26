<!-- source: https://ui.nuxt.com/components/header --> # HeaderPRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/Header.vue)

A responsive header component.

## Usage

The Header component renders a `<header>` element. Its height is defined
through a `--ui-header-height` CSS variable, which you can customize by
overriding it in your CSS:

    
    
    :root {
      --ui-header-height: --spacing(16);
    }
    

Use the `left`, `default` and `right` slots to customize the header and the
`body` or `content` slots to customize the header menu.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const route = useRoute()
    
    const items = computed<NavigationMenuItem[]>(() => [
      {
        label: 'Docs',
        to: '/getting-started',
        active: route.path.startsWith('/getting-started')
      },
      {
        label: 'Components',
        to: '/components',
        active: route.path.startsWith('/components')
      },
      {
        label: 'Roadmap',
        to: '/roadmap'
      },
      {
        label: 'Figma',
        to: 'https://www.figma.com/community/file/1288455405058138934',
        target: '_blank'
      },
      {
        label: 'Releases',
        to: 'https://github.com/nuxt/ui/releases',
        target: '_blank'
      }
    ])
    </script>
    
    <template>
      <UHeader>
        <template #title>
          <Logo class="h-6 w-auto" />
        </template>
    
        <UNavigationMenu :items="items" />
    
        <template #right>
          <UColorModeButton />
    
          <UTooltip text="Open on GitHub" :kbds="['meta', 'G']">
            <UButton
              color="neutral"
              variant="ghost"
              to="https://github.com/nuxt/ui"
              target="_blank"
              icon="i-simple-icons-github"
              aria-label="GitHub"
            />
          </UTooltip>
        </template>
      </UHeader>
    </template>
    

Expand code

In this example, we use the [NavigationMenu](/components/navigation-menu)
component to render the header links in the center.

### Title

Use the `title` prop to change the title of the header. Defaults to `Nuxt UI
Pro`.

title

    
    
    <template>
      <UHeader title="Nuxt UI Pro" />
    </template>
    

You can also use the `title` slot to add your own logo.

    
    
    <template>
      <UHeader>
        <template #title>
          <Logo class="h-6 w-auto" />
        </template>
      </UHeader>
    </template>
    

### To

Use the `to` prop to change the link of the title. Defaults to `/`.

to

    
    
    <template>
      <UHeader to="/getting-started" />
    </template>
    

You can also use the `left` slot to override the link entirely.

    
    
    <template>
      <UHeader>
        <template #left>
          <NuxtLink to="/getting-started">
            <Logo class="h-6 w-auto" />
          </NuxtLink>
        </template>
      </UHeader>
    </template>
    

### Mode

Use the `mode` prop to change the mode of the header menu. Defaults to
`modal`.

Use the `body` slot to fill the menu body (under the header) or the `content`
slot to fill the entire menu.

You can use the `menu` prop to customize the menu of the header, it will adapt
depending on the mode you choose.

mode

drawer

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const route = useRoute()
    
    const items = computed<NavigationMenuItem[]>(() => [{
      label: 'Docs',
      to: '/getting-started',
      icon: 'i-lucide-book-open',
      active: route.path.startsWith('/getting-started')
    }, {
      label: 'Components',
      to: '/components',
      icon: 'i-lucide-box',
      active: route.path.startsWith('/components')
    }, {
      label: 'Roadmap',
      icon: 'i-lucide-map',
      to: '/roadmap'
    }, {
      label: 'Figma',
      icon: 'i-simple-icons-figma',
      to: 'https://www.figma.com/community/file/1288455405058138934',
      target: '_blank'
    }, {
      label: 'Releases',
      icon: 'i-lucide-rocket',
      to: 'https://github.com/nuxt/ui/releases',
      target: '_blank'
    }])
    </script>
    
    <template>
      <UHeader>
        <template #title>
          <Logo class="h-6 w-auto" />
        </template>
    
        <UNavigationMenu :items="items" />
    
        <template #right>
          <UColorModeButton />
    
          <UTooltip text="Open on GitHub" :kbds="['meta', 'G']">
            <UButton
              color="neutral"
              variant="ghost"
              to="https://github.com/nuxt/ui"
              target="_blank"
              icon="i-simple-icons-github"
              aria-label="GitHub"
            />
          </UTooltip>
        </template>
    
        <template #body>
          <UNavigationMenu :items="items" orientation="vertical" class="-mx-2.5" />
        </template>
      </UHeader>
    </template>
    

Expand code

### Toggle

Use the `toggle` prop to customize the toggle button displayed on mobile.

You can pass any property from the [Button](/components/button) component to
customize it.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const route = useRoute()
    
    const items = computed<NavigationMenuItem[]>(() => [{
      label: 'Docs',
      to: '/getting-started',
      icon: 'i-lucide-book-open',
      active: route.path.startsWith('/getting-started')
    }, {
      label: 'Components',
      to: '/components',
      icon: 'i-lucide-box',
      active: route.path.startsWith('/components')
    }, {
      label: 'Roadmap',
      icon: 'i-lucide-map',
      to: '/roadmap'
    }, {
      label: 'Figma',
      icon: 'i-simple-icons-figma',
      to: 'https://www.figma.com/community/file/1288455405058138934',
      target: '_blank'
    }, {
      label: 'Releases',
      icon: 'i-lucide-rocket',
      to: 'https://github.com/nuxt/ui/releases',
      target: '_blank'
    }])
    </script>
    
    <template>
      <UHeader
        :toggle="{
          color: 'primary',
          variant: 'subtle',
          class: 'rounded-full'
        }"
      >
        <template #title>
          <Logo class="h-6 w-auto" />
        </template>
    
        <UNavigationMenu :items="items" />
    
        <template #right>
          <UColorModeButton />
    
          <UTooltip text="Open on GitHub" :kbds="['meta', 'G']">
            <UButton
              color="neutral"
              variant="ghost"
              to="https://github.com/nuxt/ui"
              target="_blank"
              icon="i-simple-icons-github"
              aria-label="GitHub"
            />
          </UTooltip>
        </template>
    
        <template #body>
          <UNavigationMenu :items="items" orientation="vertical" class="-mx-2.5" />
        </template>
      </UHeader>
    </template>
    

Expand code

### Toggle Side

Use the `toggle-side` prop to change the side of the toggle button. Defaults
to `right`.

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const route = useRoute()
    
    const items = computed<NavigationMenuItem[]>(() => [{
      label: 'Docs',
      to: '/getting-started',
      icon: 'i-lucide-book-open',
      active: route.path.startsWith('/getting-started')
    }, {
      label: 'Components',
      to: '/components',
      icon: 'i-lucide-box',
      active: route.path.startsWith('/components')
    }, {
      label: 'Roadmap',
      icon: 'i-lucide-map',
      to: '/roadmap'
    }, {
      label: 'Figma',
      icon: 'i-simple-icons-figma',
      to: 'https://www.figma.com/community/file/1288455405058138934',
      target: '_blank'
    }, {
      label: 'Releases',
      icon: 'i-lucide-rocket',
      to: 'https://github.com/nuxt/ui/releases',
      target: '_blank'
    }])
    </script>
    
    <template>
      <UHeader toggle-side="left">
        <template #title>
          <Logo class="h-6 w-auto" />
        </template>
    
        <UNavigationMenu :items="items" />
    
        <template #right>
          <UColorModeButton />
    
          <UTooltip text="Open on GitHub" :kbds="['meta', 'G']">
            <UButton
              color="neutral"
              variant="ghost"
              to="https://github.com/nuxt/ui"
              target="_blank"
              icon="i-simple-icons-github"
              aria-label="GitHub"
            />
          </UTooltip>
        </template>
    
        <template #body>
          <UNavigationMenu :items="items" orientation="vertical" class="-mx-2.5" />
        </template>
      </UHeader>
    </template>
    

Expand code

## Examples

### Within `app.vue`

Use the Header component in your `app.vue` or in a layout:

app.vue

    
    
    <script setup lang="ts">
    import type { NavigationMenuItem } from '@nuxt/ui'
    
    const route = useRoute()
    
    const items = computed<NavigationMenuItem[]>(() => [{
      label: 'Docs',
      to: '/getting-started',
      active: route.path.startsWith('/getting-started')
    }, {
      label: 'Components',
      to: '/components',
      active: route.path.startsWith('/components')
    }, {
      label: 'Roadmap',
      to: '/roadmap'
    }, {
      label: 'Figma',
      to: 'https://www.figma.com/community/file/1288455405058138934',
      target: '_blank'
    }, {
      label: 'Releases',
      to: 'https://github.com/nuxt/ui/releases',
      target: '_blank'
    }])
    </script>
    
    <template>
      <UApp>
        <UHeader>
          <template #title>
            <Logo class="h-6 w-auto" />
          </template>
    
          <UNavigationMenu :items="items" />
    
          <template #right>
            <UColorModeButton />
    
            <UButton
              color="neutral"
              variant="ghost"
              to="https://github.com/nuxt/ui"
              target="_blank"
              icon="i-simple-icons-github"
              aria-label="GitHub"
            />
          </template>
    
          <template #body>
            <UNavigationMenu :items="items" orientation="vertical" class="-mx-2.5" />
          </template>
        </UHeader>
    
        <UMain>
          <NuxtLayout>
            <NuxtPage />
          </NuxtLayout>
        </UMain>
    
        <UFooter />
      </UApp>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'header'`| `any`The element or component this component should render
as.  
`open`| | `boolean`  
`title`| `'Nuxt UI Pro'`| ` string`  
`to`| `'/'`| ` string`  
`mode`| `'modal'`| ` "modal" | "slideover" | "drawer"`The mode of the header menu.  
`menu`| | ` ModalProps | SlideoverProps | DrawerProps`The props for the header menu component.Show properties

  * `title?: string`
  * `description?: string`
  * `content?: (DialogContentProps & Partial<EmitsToProps<DialogContentImplEmits>>)`The content of the modal.
  * `overlay?: boolean`Render an overlay behind the modal. Defaults to `true`.
  * `transition?: boolean`Animate the modal when opening or closing. Defaults to `true`.
  * `fullscreen?: boolean`When `true`, the modal will take up the full screen. Defaults to `false`.
  * `portal?: string | boolean | HTMLElement`Render the modal in a portal. Defaults to `true`.
  * `close?: boolean | Partial<ButtonProps>`Display a close button to dismiss the modal. `{ size: 'md', color: 'neutral', variant: 'ghost' }` Defaults to `true`.
  * `closeIcon?: string`The icon displayed in the close button. Defaults to `appConfig.ui.icons.close`.
  * `dismissible?: boolean`When `false`, the modal will not close when clicking outside or pressing escape. Defaults to `true`.
  * `class?: any`
  * `ui?: { overlay?: ClassNameValue; content?: ClassNameValue; header?: ClassNameValue; wrapper?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; close?: ClassNameValue; }`
  * `open?: boolean`The controlled open state of the dialog. Can be binded as `v-model:open`.
  * `defaultOpen?: boolean`The open state of the dialog when it is initially rendered. Use when you do not need to control its open state.
  * `modal?: boolean`The modality of the dialog When set to `true`,   
interaction with outside elements will be disabled and only dialog content
will be visible to screen readers.

  * `title?: string`
  * `description?: string`
  * `content?: (DialogContentProps & Partial<EmitsToProps<DialogContentImplEmits>>)`The content of the modal.
  * `overlay?: boolean`Render an overlay behind the modal. Defaults to `true`.
  * `transition?: boolean`Animate the modal when opening or closing. Defaults to `true`.
  * `side?: "top" | "bottom" | "right" | "left"`The side of the slideover. Defaults to `'right'`.
  * `portal?: string | boolean | HTMLElement`Render the modal in a portal. Defaults to `true`.
  * `close?: boolean | Partial<ButtonProps>`Display a close button to dismiss the modal. `{ size: 'md', color: 'neutral', variant: 'ghost' }` Defaults to `true`.
  * `closeIcon?: string`The icon displayed in the close button. Defaults to `appConfig.ui.icons.close`.
  * `dismissible?: boolean`When `false`, the modal will not close when clicking outside or pressing escape. Defaults to `true`.
  * `class?: any`
  * `ui?: { overlay?: ClassNameValue; content?: ClassNameValue; header?: ClassNameValue; wrapper?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; close?: ClassNameValue; }`
  * `open?: boolean`The controlled open state of the dialog. Can be binded as `v-model:open`.
  * `defaultOpen?: boolean`The open state of the dialog when it is initially rendered. Use when you do not need to control its open state.
  * `modal?: boolean`The modality of the dialog When set to `true`,   
interaction with outside elements will be disabled and only dialog content
will be visible to screen readers.

  * `as?: any`The element or component this component should render as. Defaults to `'div'`.
  * `title?: string`
  * `description?: string`
  * `inset?: boolean`Whether to inset the drawer from the edges. Defaults to `false`.
  * `content?: (DialogContentProps & Partial<EmitsToProps<DialogContentImplEmits>>)`The content of the modal.
  * `overlay?: boolean`Render an overlay behind the modal. Defaults to `true`.
  * `handle?: boolean`Render a handle on the drawer. Defaults to `true`.
  * `portal?: string | boolean | HTMLElement`Render the modal in a portal. Defaults to `true`.
  * `class?: any`
  * `ui?: { overlay?: ClassNameValue; content?: ClassNameValue; handle?: ClassNameValue; container?: ClassNameValue; header?: ClassNameValue; title?: ClassNameValue; description?: ClassNameValue; body?: ClassNameValue; footer?: ClassNameValue; }`
  * `fixed?: boolean`When `true`, don't move the drawer upwards if there's space, but rather only change it's height so it's fully scrollable when the keyboard is open
  * `open?: boolean`
  * `defaultOpen?: boolean`The open state of the dialog when it is initially rendered. Use when you do not need to control its open state.
  * `modal?: boolean`The modality of the dialog When set to `true`,   
interaction with outside elements will be disabled and only dialog content
will be visible to screen readers.

  * `activeSnapPoint?: string | number | null`
  * `closeThreshold?: number`Number between 0 and 1 that determines when the drawer should be closed. Example: threshold of 0.5 would close the drawer if the user swiped for 50% of the height of the drawer or more.
  * `shouldScaleBackground?: boolean`
  * `setBackgroundColorOnScale?: boolean`When `false` we don't change body's background color when the drawer is open.
  * `scrollLockTimeout?: number`Duration for which the drawer is not draggable after scrolling content inside of the drawer.
  * `dismissible?: boolean`When `false`, the modal will not close when clicking outside or pressing escape. Defaults to `true`.
  * `nested?: boolean`
  * `direction?: DrawerDirection`Direction of the drawer. Can be `top` or `bottom`, `left`, `right`.
  * `noBodyStyles?: boolean`When `true` the `body` doesn't get any styles assigned from Vaul
  * `handleOnly?: boolean`When `true` only allows the drawer to be dragged by the `<Drawer.Handle />` component.
  * `preventScrollRestoration?: boolean`
  * `snapPoints?: (string | number)[]`Array of numbers from 0 to 100 that corresponds to % of the screen a given snap point should take up. Should go from least visible. Example `[0.2, 0.5, 0.8]`. You can also use px values, which doesn't take screen height into account.

  
`toggle`| `true`| `boolean | Partial<ButtonProps>`Customize the toggle button to open the header menu displayed when the `content` slot is used. `{ color: 'neutral', variant: 'ghost' }`  
`toggleSide`| `'right'`| ` "right" | "left"`The side to render the toggle button on.  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; left?: ClassNameValue; center?: ClassNameValue; right?: ClassNameValue; ... 5 more ...; body?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`title`| `{}`  
`left`| `{}`  
`default`| `{}`  
`right`| `{}`  
`toggle`| `{ open: boolean; toggle: () => void; }`  
`top`| `{}`  
`bottom`| `{}`  
`body`| `{}`  
`content`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:open`| `boolean`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        header: {
          slots: {
            root: 'bg-default/75 backdrop-blur border-b border-default h-(--ui-header-height) sticky top-0 z-50',
            container: 'flex items-center justify-between gap-3 h-full',
            left: 'lg:flex-1 flex items-center gap-1.5',
            center: 'hidden lg:flex',
            right: 'flex items-center justify-end lg:flex-1 gap-1.5',
            title: 'shrink-0 font-bold text-xl text-highlighted flex items-end gap-1.5',
            toggle: 'lg:hidden',
            content: 'lg:hidden',
            overlay: 'lg:hidden',
            header: 'px-4 sm:px-6 h-(--ui-header-height) shrink-0 flex items-center justify-between gap-3',
            body: 'p-4 sm:p-6 overflow-y-auto'
          },
          variants: {
            toggleSide: {
              left: {
                toggle: '-ms-1.5'
              },
              right: {
                toggle: '-me-1.5'
              }
            }
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
          uiPro: {
            header: {
              slots: {
                root: 'bg-default/75 backdrop-blur border-b border-default h-(--ui-header-height) sticky top-0 z-50',
                container: 'flex items-center justify-between gap-3 h-full',
                left: 'lg:flex-1 flex items-center gap-1.5',
                center: 'hidden lg:flex',
                right: 'flex items-center justify-end lg:flex-1 gap-1.5',
                title: 'shrink-0 font-bold text-xl text-highlighted flex items-end gap-1.5',
                toggle: 'lg:hidden',
                content: 'lg:hidden',
                overlay: 'lg:hidden',
                header: 'px-4 sm:px-6 h-(--ui-header-height) shrink-0 flex items-center justify-between gap-3',
                body: 'p-4 sm:p-6 overflow-y-auto'
              },
              variants: {
                toggleSide: {
                  left: {
                    toggle: '-ms-1.5'
                  },
                  right: {
                    toggle: '-me-1.5'
                  }
                }
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
          uiPro: {
            header: {
              slots: {
                root: 'bg-default/75 backdrop-blur border-b border-default h-(--ui-header-height) sticky top-0 z-50',
                container: 'flex items-center justify-between gap-3 h-full',
                left: 'lg:flex-1 flex items-center gap-1.5',
                center: 'hidden lg:flex',
                right: 'flex items-center justify-end lg:flex-1 gap-1.5',
                title: 'shrink-0 font-bold text-xl text-highlighted flex items-end gap-1.5',
                toggle: 'lg:hidden',
                content: 'lg:hidden',
                overlay: 'lg:hidden',
                header: 'px-4 sm:px-6 h-(--ui-header-height) shrink-0 flex items-center justify-between gap-3',
                body: 'p-4 sm:p-6 overflow-y-auto'
              },
              variants: {
                toggleSide: {
                  left: {
                    toggle: '-ms-1.5'
                  },
                  right: {
                    toggle: '-me-1.5'
                  }
                }
              }
            }
          }
        })
      ]
    })
    

Expand code

[FormFieldA wrapper for form elements that provides validation and error
handling.](/components/form-field)[IconA component to display any icon from
Iconify.](/components/icon)

