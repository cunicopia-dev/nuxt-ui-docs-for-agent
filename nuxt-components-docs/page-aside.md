<!-- source: https://ui.nuxt.com/components/page-aside --> # PageAsidePRO

[GitHub](https://github.com/nuxt/ui-
pro/tree/v3/src/runtime/components/PageAside.vue)

A sticky aside to display your page navigation.

## Usage

The PageAside component is a sticky `<aside>` element that is only displayed
starting from the [`lg` breakpoint](https://tailwindcss.com/docs/breakpoints).

The PageAside component uses the `--ui-header-height` CSS variable to position
itself correctly below the [Header](/components/header). You can customize its
height by overriding the variable in your CSS:

    
    
    :root {
      --ui-header-height: --spacing(16);
    }
    

Use it inside the `left` or `right` slot of the [Page](/components/page)
component:

    
    
    <template>
      <UPage>
        <template #left>
          <UPageAside />
        </template>
      </UPage>
    </template>
    

## Examples

While these examples use [Nuxt Content](https://content.nuxt.com), the
components can be integrated with any content management system.

### Within a layout

Use the PageAside component in a layout to display the navigation:

layouts/docs.vue

    
    
    <script setup lang="ts">
    import type { ContentNavigationItem } from '@nuxt/content'
    
    const navigation = inject<Ref<ContentNavigationItem[]>>('navigation')
    </script>
    
    <template>
      <UPage>
        <template #left>
          <UPageAside>
            <UContentNavigation :navigation="navigation" />
          </UPageAside>
        </template>
    
        <slot />
      </UPage>
    </template>
    

In this example, we use the `ContentNavigation` component to display the
navigation injected in `app.vue`.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'aside'`| `any`  
`ui`| | ` { root?: ClassNameValue; container?: ClassNameValue; top?: ClassNameValue; topHeader?: ClassNameValue; topBody?: ClassNameValue; topFooter?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`top`| `{}`  
`default`| `{}`  
`bottom`| `{}`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      uiPro: {
        pageAside: {
          slots: {
            root: 'hidden overflow-y-auto lg:block lg:max-h-[calc(100vh-var(--ui-header-height))] lg:sticky lg:top-(--ui-header-height) py-8 lg:ps-4 lg:-ms-4 lg:pe-6.5',
            container: 'relative',
            top: 'sticky -top-8 -mt-8 pointer-events-none z-[1]',
            topHeader: 'h-8 bg-default -mx-4 px-4',
            topBody: 'bg-default relative pointer-events-auto flex flex-col -mx-4 px-4',
            topFooter: 'h-8 bg-gradient-to-b from-default -mx-4 px-4'
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
            pageAside: {
              slots: {
                root: 'hidden overflow-y-auto lg:block lg:max-h-[calc(100vh-var(--ui-header-height))] lg:sticky lg:top-(--ui-header-height) py-8 lg:ps-4 lg:-ms-4 lg:pe-6.5',
                container: 'relative',
                top: 'sticky -top-8 -mt-8 pointer-events-none z-[1]',
                topHeader: 'h-8 bg-default -mx-4 px-4',
                topBody: 'bg-default relative pointer-events-auto flex flex-col -mx-4 px-4',
                topFooter: 'h-8 bg-gradient-to-b from-default -mx-4 px-4'
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
            pageAside: {
              slots: {
                root: 'hidden overflow-y-auto lg:block lg:max-h-[calc(100vh-var(--ui-header-height))] lg:sticky lg:top-(--ui-header-height) py-8 lg:ps-4 lg:-ms-4 lg:pe-6.5',
                container: 'relative',
                top: 'sticky -top-8 -mt-8 pointer-events-none z-[1]',
                topHeader: 'h-8 bg-default -mx-4 px-4',
                topBody: 'bg-default relative pointer-events-auto flex flex-col -mx-4 px-4',
                topFooter: 'h-8 bg-gradient-to-b from-default -mx-4 px-4'
              }
            }
          }
        })
      ]
    })
    

Expand code

[PageAnchorsA list of anchors to be displayed in the page.](/components/page-
anchors)[PageBodyThe main content of your page.](/components/page-body)

